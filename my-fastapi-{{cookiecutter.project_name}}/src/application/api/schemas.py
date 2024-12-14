# endregion-------------------------------------------------------------------------
# region APPLICATION SCHEMAS
# ----------------------------------------------------------------------------------
from pydantic import BaseModel, ConfigDict, Field

from typing import Annotated


class ParentSchema(BaseModel):
    """-----------------------------------------------------------------------------
    The Parent Schema with custom configuration.
    -----------------------------------------------------------------------------"""

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        protected_namespaces=(),
    )


class ErrorSchemaDetail(ParentSchema):
    """-----------------------------------------------------------------------------
    The Error Schema Detail.
    -----------------------------------------------------------------------------"""

    error: Annotated[str, Field()]
    name: Annotated[str, Field()]


class ErrorSchema(ParentSchema):
    """-----------------------------------------------------------------------------
    The Error Schema.
    -----------------------------------------------------------------------------"""

    detail: Annotated[ErrorSchemaDetail, Field()]


# endregion-------------------------------------------------------------------------
