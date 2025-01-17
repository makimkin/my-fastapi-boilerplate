# endregion-------------------------------------------------------------------------
# region FASTAPI CONCURRENT CONNECTION MANAGER
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from fastapi import WebSocket

from infrastructure.connection_manager.common.concurrent import (
    ConnectionManagerConcurrent,
)

from .base import FastAPIConnectionManagerBase


@dataclass
class FastAPIConnectionManagerConcurrent(
    FastAPIConnectionManagerBase, ConnectionManagerConcurrent[WebSocket]
): ...


# endregion-------------------------------------------------------------------------
