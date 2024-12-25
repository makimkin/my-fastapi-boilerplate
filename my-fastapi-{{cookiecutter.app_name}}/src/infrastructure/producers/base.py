# endregion-------------------------------------------------------------------------
# region BASE PRODUCER
# ----------------------------------------------------------------------------------
import logging

from abc import ABC, abstractmethod
from dataclasses import dataclass

logger = logging.getLogger("app")


@dataclass
class ProducerBase(ABC):
    @abstractmethod
    async def send_message(self, topic: str, value: bytes) -> None: ...

    async def close(self) -> None:
        logger.info("Closing message producer")

        await self._close()

    @abstractmethod
    async def _close(self) -> None: ...

    async def connect(self) -> None:
        logger.info("Connecting message producer")

        await self._connect()

    @abstractmethod
    async def _connect(self) -> None: ...


# endregion-------------------------------------------------------------------------
