# endregion-------------------------------------------------------------------------
# region API EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import abstractmethod

from interface.exceptions import InterfaceExceptionBase


@dataclass(frozen=False)
class APIExceptionBase(InterfaceExceptionBase):
    @property
    @abstractmethod
    def message(self) -> str:
        return "API exception occured"


# endregion-------------------------------------------------------------------------
