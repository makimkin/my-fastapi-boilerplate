# endregion-------------------------------------------------------------------------
# region PRESENTATION BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import abstractmethod

from application.exceptions import ApplicationExceptionBase



@dataclass(frozen=False)
class PresentationExceptionBase(ApplicationExceptionBase):
    @property
    @abstractmethod
    def message(self):
        return "Presentation error occured"


# endregion-------------------------------------------------------------------------
