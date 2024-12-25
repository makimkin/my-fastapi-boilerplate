# endregion-------------------------------------------------------------------------
# region BASE COMMANDS
# ----------------------------------------------------------------------------------
import logging

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger("app")


@dataclass(frozen=True)
class CommandBase(ABC): ...  # noqa: B024


@dataclass(frozen=True)
class CommandHandlerBase[C: CommandBase, R: Any](ABC):
    async def handle(self, command: C) -> R:
        logger.info(
            f"{self.__class__.__name__} handles command {command.__class__.__name__}"
        )

        return await self._handle(command)

    @abstractmethod
    async def _handle(self, command: C) -> R: ...


# endregion-------------------------------------------------------------------------
