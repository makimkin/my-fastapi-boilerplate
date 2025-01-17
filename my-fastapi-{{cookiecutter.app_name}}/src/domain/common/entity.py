# endregion-------------------------------------------------------------------------
# region BASE ENTITY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from .value_object import EntityId
from .event import EventBase


KEY_ENTITY_ID = "id"


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


@dataclass(eq=False, kw_only=True)
class EntityBaseWithId(EntityBase, ABC):
    id: EntityId = field(default_factory=lambda: EntityId.create())

    def __hash__(self) -> int:
        return hash(self.id.as_raw())

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.id == o.id

    def __post_init__(self):
        if not self.id:
            raise ValueError("Entity id must be greater than zero.")

    def to_dict(self) -> dict:
        return {KEY_ENTITY_ID: self.id.as_raw(), **super().to_dict()}


# endregion-------------------------------------------------------------------------
