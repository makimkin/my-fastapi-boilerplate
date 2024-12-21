# endregion-------------------------------------------------------------------------
# region BASE EVENTS
# ----------------------------------------------------------------------------------
import datetime
import logging
import uuid

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from infrastructure.producers.base import ProducerBase

logger = logging.getLogger("app")


@dataclass(frozen=True)
class EventBase(ABC):
    event_id: uuid.UUID = field(init=False, kw_only=True, default_factory=uuid.uuid4)
    event_timestamp: datetime.datetime = field(
        default_factory=datetime.datetime.now,
        kw_only=True,
        init=False,
    )

    @abstractmethod
    def to_bytes(self) -> bytes: ...

    @abstractmethod
    def to_dict(self) -> dict:
        return {
            "event_id": str(self.event_id),
            "event_timestamp": self.event_timestamp.isoformat(),
        }


@dataclass(frozen=True)
class EventHandlerBase[E: EventBase](ABC):
    producer: ProducerBase
    topic: str

    async def handle(self, event: E) -> None:
        logger.info(
            f"{self.__class__.__name__} handles event {event.__class__.__name__}"
        )

        return await self._handle(event)

    @abstractmethod
    async def _handle(self, event: E) -> None: ...


# endregion-------------------------------------------------------------------------
