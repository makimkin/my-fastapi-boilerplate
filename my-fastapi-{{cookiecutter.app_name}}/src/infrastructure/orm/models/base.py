# endregion-------------------------------------------------------------------------
# region BASE MODELS
# ----------------------------------------------------------------------------------
from sqlalchemy.orm import DeclarativeBase


class ModelBase(DeclarativeBase):
    __allow_unmapped__ = True


# endregion-------------------------------------------------------------------------
