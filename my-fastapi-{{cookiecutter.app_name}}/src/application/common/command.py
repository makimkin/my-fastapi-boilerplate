# endregion-------------------------------------------------------------------------
# region BASE COMMANDS
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from domain.common.event import EventBase

logger = logging.getLogger("app")


@dataclass(frozen=True)
class CommandBase(ABC): ...  # noqa: B024


@dataclass(frozen=True)
class CommandHandlerBase[C: CommandBase, R](ABC):
    _events: list[EventBase] = field(default_factory=list, kw_only=True)

    async def handle(self, command: C) -> R:
        logger.info(
            f"{self.__class__.__name__} handles command {command.__class__.__name__}"
        )

        return await self._handle(command)

    def catch_events(self, events: list[EventBase]) -> None:
        self._events.extend(events)

    @abstractmethod
    async def _handle(self, command: C) -> R: ...


# endregion-------------------------------------------------------------------------
