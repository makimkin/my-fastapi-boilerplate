# endregion-------------------------------------------------------------------------
# region BASE MODELS
# ----------------------------------------------------------------------------------
from sqlalchemy.orm import DeclarativeBase


PRODUCT_TABLE_NAME = "products"


class Base(DeclarativeBase):
    __allow_unmapped__ = True


# endregion-------------------------------------------------------------------------
