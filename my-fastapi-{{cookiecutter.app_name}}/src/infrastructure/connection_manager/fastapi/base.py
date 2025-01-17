# endregion-------------------------------------------------------------------------
# region FASTAPI BASE CONNECTION MANAGER
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass
from abc import ABC

from fastapi import WebSocket, WebSocketDisconnect

from ..common.base import ConnectionManagerBase

logger = logging.getLogger("app")


@dataclass
class FastAPIConnectionManagerBase(ConnectionManagerBase[WebSocket], ABC):
    async def send(self, connection: WebSocket, message: dict) -> bool:
        try:
            return await super().send(connection, message)
        except WebSocketDisconnect:
            logger.error(f"Connection {connection} disconnected")

            await self.disconnect(connection)

            return False


# endregion-------------------------------------------------------------------------
