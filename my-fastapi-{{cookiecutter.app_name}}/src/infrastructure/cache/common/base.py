# endregion-------------------------------------------------------------------------
# region BASE CACHE
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class CacheBase(ABC):
    @abstractmethod
    async def get(self, key: str) -> Any | None:
        pass

    @abstractmethod
    async def set(
        self,
        key: str,
        value: Any,
        *,
        expiration_milliseconds: int | None = None,
    ) -> None:
        pass

    @abstractmethod
    async def get_keys(self, pattern: str) -> list[str]:
        pass

    @abstractmethod
    async def get_values(
        self,
        keys: list[str],
        batch_size: int = 100,
    ) -> dict[str, Any | None]:
        pass


# endregion-------------------------------------------------------------------------
