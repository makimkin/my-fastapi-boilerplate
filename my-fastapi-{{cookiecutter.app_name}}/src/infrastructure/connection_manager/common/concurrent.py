# endregion-------------------------------------------------------------------------
# region CONCURRENT CONNECTION MANAGER
# ----------------------------------------------------------------------------------
import asyncio
import logging

from dataclasses import dataclass, field
from abc import ABC

from .base import ConnectionManagerBase, Connection


logger = logging.getLogger("app")


@dataclass
class ConnectionManagerConcurrent[T: Connection](ConnectionManagerBase[T], ABC):
    lock: asyncio.Lock = field(
        default_factory=asyncio.Lock,
        kw_only=True,
    )

    async def _connect(self, connection: T) -> None:
        await connection.accept()

        async with self.lock:
            self.connections.append(connection)

    async def _disconnect(self, connection: T) -> None:
        try:
            await connection.close()
        except RuntimeError:
            pass

        if connection in self.connections:
            async with self.lock:
                self.connections.remove(connection)

    async def _send(self, connection: T, message: dict) -> bool:
        if connection not in self.connections:
            logger.error(f"Connection {connection} not found")
            return False

        await connection.send_json(message)

        return True

    async def _close(self) -> None:
        for connection in self.connections:
            await self.disconnect(connection)


# endregion-------------------------------------------------------------------------
