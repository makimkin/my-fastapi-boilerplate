# endregion-------------------------------------------------------------------------
# region MEMORY REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from abc import ABC

from .base import RepositoryBase


@dataclass
class RepositoryMemory[T](RepositoryBase, ABC):
    _saved: list[T] = field(default_factory=list)

    @property
    def saved(self) -> list[T]:
        """-------------------------------------------------------------------------
        Get a copy of the saved items.
        -------------------------------------------------------------------------"""
        return [*self._saved]

    @saved.setter
    def saved(self, items: list[T]) -> None:
        """-------------------------------------------------------------------------
        Set the saved items.
        -------------------------------------------------------------------------"""
        self._saved = items


# endregion-------------------------------------------------------------------------
