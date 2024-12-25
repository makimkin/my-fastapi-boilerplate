# endregion-------------------------------------------------------------------------
# region INFRASTRUCTURE BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from exceptions import ExceptionBase


@dataclass(frozen=False)
class InfrastructureExceptionBase(ExceptionBase, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Infrastructure exception occured"


# endregion-------------------------------------------------------------------------
