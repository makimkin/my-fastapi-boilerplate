# endregion-------------------------------------------------------------------------
# region APPLICATION BASE EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass


@dataclass(eq=False)
class BaseApplicationException(Exception, metaclass=type):
    @property
    def message(self):
        return "Application error occured"


# endregion-------------------------------------------------------------------------
