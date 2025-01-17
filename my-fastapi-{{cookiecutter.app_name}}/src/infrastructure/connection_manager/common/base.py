# endregion-------------------------------------------------------------------------
# region BASE CONNECTION MANAGER
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any, Protocol

from infrastructure.common.base import InfrastructureBase

logger = logging.getLogger("app")


class Connection(Protocol):
    async def accept(self) -> None: ...

    async def close(self) -> None: ...

    async def send_json(self, data: Any, mode: str = "text") -> None: ...


@dataclass
class ConnectionManagerBase[T: Connection](InfrastructureBase, ABC):
    connections: list[T] = field(
        default_factory=list,
        kw_only=True,
    )

    async def connect(self, connection: T) -> None:
        """-------------------------------------------------------------------------
        Connect a connection and add it to the list of connections.
        -------------------------------------------------------------------------"""
        await self._connect(connection)

        logger.info(
            f"Connection {connection} started. Total connections: {len(self.connections)}"
        )

    async def disconnect(self, connection: T) -> None:
        """-------------------------------------------------------------------------
        Disconnect a connection and remove it from the list of connections.
        -------------------------------------------------------------------------"""
        await self._disconnect(connection)

        logger.info(
            f"Connection {connection} closed. Total connections: {len(self.connections)}"
        )

    async def send(self, connection: T, message: dict) -> bool:
        """-------------------------------------------------------------------------
        Send a message to a connection and returns True if successful.
        -------------------------------------------------------------------------"""
        logger.info(f"Connection {connection} sent message {message}")

        try:
            return await self._send(connection, message)
        except RuntimeError:
            logger.info(f"RuntimeError sending message to {connection}")

            await self.disconnect(connection)

            return False

    async def close(self) -> None:
        """-------------------------------------------------------------------------
        Close all connections.
        -------------------------------------------------------------------------"""
        logger.info(f"Closing {len(self.connections)} connections")

        await self._close()

    async def broadcast(self, message: dict) -> None:
        """-------------------------------------------------------------------------
        Broadcast a message to all connections.
        -------------------------------------------------------------------------"""
        for connection in self.connections:
            await self._send(connection, message)

    @abstractmethod
    async def _connect(self, connection: T) -> None: ...

    @abstractmethod
    async def _disconnect(self, connection: T) -> None: ...

    @abstractmethod
    async def _send(self, connection: T, message: dict) -> bool: ...

    @abstractmethod
    async def _close(self) -> None: ...

    async def check_health(self) -> bool:
        return True


# endregion-------------------------------------------------------------------------
