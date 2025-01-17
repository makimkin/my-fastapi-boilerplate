# endregion-------------------------------------------------------------------------
# region APPLICATION SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from pydantic import AfterValidator, Field, BaseModel, ConfigDict

from domain.common.value_object import EntityId

from .validators import validate_str_value_object


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
# region FIELDS
# ----------------------------------------------------------------------------------
FIELD_ID = Annotated[
    EntityId | str,
    Field(description="The ID field"),
    AfterValidator(validate_str_value_object),
]

# endregion-------------------------------------------------------------------------
