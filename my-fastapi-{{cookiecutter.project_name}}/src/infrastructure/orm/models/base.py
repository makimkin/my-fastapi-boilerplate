# endregion-------------------------------------------------------------------------
# region BASE MODELS
# ----------------------------------------------------------------------------------
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __allow_unmapped__ = True


# endregion-------------------------------------------------------------------------
