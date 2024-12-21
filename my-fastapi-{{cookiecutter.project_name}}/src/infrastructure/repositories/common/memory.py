# endregion-------------------------------------------------------------------------
# region MEMORY REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from abc import ABC

from .base import RepositoryBase


@dataclass
class RepositoryMemory[T](RepositoryBase, ABC):
    saved: list[T] = field(default_factory=list)


# endregion-------------------------------------------------------------------------
