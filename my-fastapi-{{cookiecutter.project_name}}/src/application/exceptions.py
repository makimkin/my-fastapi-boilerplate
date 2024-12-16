# endregion-------------------------------------------------------------------------
# region APPLICATION BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseApplicationException(Exception):
    @property
    def message(self):
        return "Application error occured"


# endregion-------------------------------------------------------------------------
