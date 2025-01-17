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
# region VALUIE OBJECTS EXCEPTIONS
# ----------------------------------------------------------------------------------
@dataclass(frozen=False)
class ValueObjectEntityIdIncorrectValueException(DomainExceptionBase):
    value: str

    @property
    def message(self) -> str:
        return f"EntityId value is incorrect: {self.value}"


# endregion-------------------------------------------------------------------------
