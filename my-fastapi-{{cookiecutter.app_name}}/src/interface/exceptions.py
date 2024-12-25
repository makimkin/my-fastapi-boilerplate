# endregion-------------------------------------------------------------------------
# region INTERFACE BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import abstractmethod

from application.exceptions import ApplicationExceptionBase



@dataclass(frozen=False)
class InterfaceExceptionBase(ApplicationExceptionBase):
    @property
    @abstractmethod
    def message(self):
        return "Interface error occured"


# endregion-------------------------------------------------------------------------
