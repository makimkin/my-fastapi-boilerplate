# endregion-------------------------------------------------------------------------
# region APPLICATION BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from domain.common.exceptions import ExceptionBase


@dataclass(frozen=False)
class ApplicationExceptionBase(ExceptionBase, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Application error occured"


# endregion-------------------------------------------------------------------------
