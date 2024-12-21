# endregion-------------------------------------------------------------------------
# region INFRASTRUCTURE BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from presentation.exceptions import PresentationExceptionBase


@dataclass(frozen=False)
class InfrastructureExceptionBase(PresentationExceptionBase, ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        return "Infrastructure exception occured"


# endregion-------------------------------------------------------------------------
