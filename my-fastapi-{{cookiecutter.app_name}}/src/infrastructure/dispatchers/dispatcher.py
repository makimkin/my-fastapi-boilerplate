# endregion-------------------------------------------------------------------------
# region DISPATCHERS
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass
from typing import Any, Type

from application.common.command import CommandBase, CommandHandlerBase
from application.common.query import QueryBase, QueryHandlerBase

from domain.common.event import EventBase, EventHandlerBase

from infrastructure.dispatchers.base import (
    DispatcherCommand,
    DispatcherEvent,
    DispatcherQuery,
)
from .exceptions import (
    DispatcherNoCommandHandlerFound,
    DispatcherNoEventHandlerFound,
    DispatcherNoQueryHandlerFound,
)


logger = logging.getLogger("app")


@dataclass(eq=False, kw_only=True)
class Dispatcher[C: CommandBase, CR: Any, Q: QueryBase, QR: Any, E: EventBase](
    DispatcherCommand[C, CR],
    DispatcherQuery[Q, QR],
    DispatcherEvent[E],
):
    # endregion---------------------------------------------------------------------
    # region COMMANDS
    # ------------------------------------------------------------------------------
    def register_command(self, command: Type[C], handler: CommandHandlerBase[C, CR]):
        logger.info(
            f"Registering command {command.__name__} "
            + "with handler {handler.__class__.__name__}",
        )

        self.commands_map[command.__name__].append(handler)

    async def handle_command(self, command: C) -> list[CR]:
        logger.info(f"Handling command {command.__class__.__name__}")

        handlers = self.commands_map.get(command.__class__.__name__, None)

        if handlers is None:
            raise DispatcherNoCommandHandlerFound(command.__class__.__name__)

        return [await handler.handle(command) for handler in handlers]

    # endregion---------------------------------------------------------------------
    # region QUERY
    # ------------------------------------------------------------------------------
    def register_query(self, query: type[Q], handler: QueryHandlerBase[Q, QR]):
        logger.info(
            f"Registering query {query.__name__} "
            + "with handler {handler.__class__.__name__}",
        )

        self.queries_map[query.__name__] = handler

    async def handle_query(self, query: Q) -> QR:
        logger.info(f"Handling query {query.__class__.__name__}")

        handler = self.queries_map.get(query.__class__.__name__, None)

        if handler is None:
            raise DispatcherNoQueryHandlerFound(query.__class__.__name__)

        return await handler.handle(query)

    # endregion---------------------------------------------------------------------
    # region EVENTS
    # ------------------------------------------------------------------------------
    def register_event(self, event: type[E], handler: EventHandlerBase[E]):
        logger.info(f"Registering event {event.__name__}")

        self.events_map[event.__name__].append(handler)

    async def handle_event(self, event: E) -> None:
        logger.info(f"Handling event {event.__class__.__name__}")

        handlers = self.events_map.get(event.__class__.__name__, None)

        if handlers is None:
            raise DispatcherNoEventHandlerFound(event.__class__.__name__)

        [await handler.handle(event) for handler in handlers]


# endregion-------------------------------------------------------------------------
