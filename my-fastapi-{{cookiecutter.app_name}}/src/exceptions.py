# endregion-------------------------------------------------------------------------
# region BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=False)
class ExceptionBase(Exception, ABC):
    @property
    def status_code(self) -> int | None:
        return None

    @property
    @abstractmethod
    def message(self) -> str: ...


# endregion-------------------------------------------------------------------------
