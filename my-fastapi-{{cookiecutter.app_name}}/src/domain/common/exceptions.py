# endregion-------------------------------------------------------------------------
# region DOMAIN BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=False)
class ExceptionBase(Exception, ABC):
    @property
    @abstractmethod
    def message(self) -> str: ...


@dataclass(frozen=False)
class DomainExceptionBase(ExceptionBase, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Domain error occured"


# endregion-------------------------------------------------------------------------
