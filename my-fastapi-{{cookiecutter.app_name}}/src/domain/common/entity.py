# endregion-------------------------------------------------------------------------
# region BASE ENTITY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from uuid import uuid4

from domain.common.event import EventBase


@dataclass(eq=False, kw_only=True)
class EntityBase(ABC):
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        metadata={"description": "Unique identifier"},
    )
    events: list[EventBase] = field(
        default_factory=list,
        metadata={"description": "List of events related to the entity"},
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, self.__class__) and self.oid == o.oid

    def register_event(self, event: EventBase) -> None:
        self.events.append(event)

    def pull_events(self) -> list[EventBase]:
        events = [*self.events]
        self.events.clear()

        return events

    @abstractmethod
    def to_document(self) -> dict: ...

    @classmethod
    @abstractmethod
    def from_document(cls, document: dict) -> "EntityBase": ...


# endregion-------------------------------------------------------------------------
