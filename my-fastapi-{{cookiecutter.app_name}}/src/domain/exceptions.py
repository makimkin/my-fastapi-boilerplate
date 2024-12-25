# endregion-------------------------------------------------------------------------
# region DOMAIN BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import ABC, abstractmethod

from exceptions import ExceptionBase


@dataclass(frozen=False)
class DomainExceptionBase(ExceptionBase, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Domain error occured"


# endregion-------------------------------------------------------------------------
