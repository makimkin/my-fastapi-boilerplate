# endregion-------------------------------------------------------------------------
# region BASE QUERIES
# ----------------------------------------------------------------------------------
import logging

from abc import ABC, abstractmethod
from dataclasses import dataclass

logger = logging.getLogger("app")


@dataclass(frozen=True)
class QueryBase(ABC): ...  # noqa: B024


@dataclass(frozen=True)
class QueryHandlerBase[Q: QueryBase, R](ABC):
    async def handle(self, query: Q) -> R:
        logger.info(
            f"{self.__class__.__name__} handles query {query.__class__.__name__}"
        )

        return await self._handle(query)

    @abstractmethod
    async def _handle(self, query: Q) -> R: ...


# endregion-------------------------------------------------------------------------
