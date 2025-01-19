# endregion-------------------------------------------------------------------------
# region APPLICATION SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from pydantic import Field, BaseModel, ConfigDict


class APISchema(BaseModel):
    """-----------------------------------------------------------------------------
    The API Schema with custom configuration.
    -----------------------------------------------------------------------------"""

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        protected_namespaces=(),
    )


class ErrorSchemaDetail(APISchema):
    """-----------------------------------------------------------------------------
    The Error Schema Detail.
    -----------------------------------------------------------------------------"""

    error: Annotated[str, Field()]
    name: Annotated[str, Field()]


class ErrorSchema(APISchema):
    """-----------------------------------------------------------------------------
    The Error Schema.
    -----------------------------------------------------------------------------"""

    detail: Annotated[ErrorSchemaDetail, Field()]


# endregion-------------------------------------------------------------------------
