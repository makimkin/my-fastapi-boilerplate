# endregion-------------------------------------------------------------------------
# region FASTAPI DEFAULT CONNECTION MANAGER
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from fastapi import WebSocket

from infrastructure.connection_manager.common.default import (
    ConnectionManagerDefault,
)

from .base import FastAPIConnectionManagerBase


@dataclass
class FastAPIConnectionManagerDefault(
    FastAPIConnectionManagerBase, ConnectionManagerDefault[WebSocket]
): ...


# endregion-------------------------------------------------------------------------
