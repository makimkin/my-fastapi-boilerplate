# endregion-------------------------------------------------------------------------
# region APPLICATION SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from pydantic import Field, BaseModel, ConfigDict

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
