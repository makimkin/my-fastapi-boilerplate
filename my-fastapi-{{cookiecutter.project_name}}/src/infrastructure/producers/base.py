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

    @abstractmethod
    async def close(self) -> None:
        logger.info("Closing message producer")

    @abstractmethod
    async def connect(self) -> None:
        logger.info("Connecting message producer")


# endregion-------------------------------------------------------------------------
