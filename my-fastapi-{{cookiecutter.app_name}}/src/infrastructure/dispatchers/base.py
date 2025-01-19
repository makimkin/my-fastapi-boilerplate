# endregion-------------------------------------------------------------------------
# region BASE DISPATCHERS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from collections import defaultdict
from abc import ABC, abstractmethod
from typing import Any, Type

from application.common.command import CommandBase, CommandHandlerBase
from application.common.query import QueryBase, QueryHandlerBase

from domain.common.event import EventBase, EventHandlerBase


@dataclass(eq=False, kw_only=True)
class DispatcherCommand[C: CommandBase, R: Any](ABC):
    _commands_map: dict[str, CommandHandlerBase[C, R]] = field(default_factory=dict)

    @abstractmethod
    def register_command(self, command: Type[C], handler: CommandHandlerBase[C, R]): ...

    @abstractmethod
    async def handle_command(self, command: C) -> R: ...


@dataclass(eq=False, kw_only=True)
class DispatcherQuery[Q: QueryBase, R: Any](ABC):
    _queries_map: dict[str, QueryHandlerBase[Q, R]] = field(default_factory=dict)

    @abstractmethod
    def register_query(self, query: Type[Q], handler: QueryHandlerBase[Q, R]): ...

    @abstractmethod
    async def handle_query(self, query: Q) -> R: ...


@dataclass(eq=False, kw_only=True)
class DispatcherEvent[E: EventBase](ABC):
    _events_map: dict[str, list[EventHandlerBase[E]]] = field(
        default_factory=lambda: defaultdict(list)
    )

    @abstractmethod
    def register_event(self, event: Type[E]): ...

    @abstractmethod
    async def handle_event(self, event: E): ...


# endregion-------------------------------------------------------------------------
