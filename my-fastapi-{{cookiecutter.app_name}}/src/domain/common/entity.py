# endregion-------------------------------------------------------------------------
# region BASE ENTITY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from .event import EventBase


@dataclass(eq=False, kw_only=True)
class EntityBase(ABC):
    _events: list[EventBase] = field(default_factory=list)

    def register_event(self, event: EventBase) -> None:
        self._events.append(event)

    def pull_events(self) -> list[EventBase]:
        events = [*self._events]
        self._events.clear()

        return events

    @abstractmethod
    def to_dict(self) -> dict:
        return {}

    @classmethod
    @abstractmethod
    def from_dict(cls, document: dict) -> "EntityBase": ...


# endregion-------------------------------------------------------------------------
