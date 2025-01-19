# endregion-------------------------------------------------------------------------
# region APPLICATION FIELDS
# ----------------------------------------------------------------------------------
from typing import Annotated

from pydantic import AfterValidator, Field

from domain.common.value_object import EntityCreatedAt, EntityId

from .validators import (
    validate_str_value_object,
    validate_datetime_value_object,
)


# endregion-------------------------------------------------------------------------
# region ENTITY
# ----------------------------------------------------------------------------------
FIELD_ENTITY_CREATED_AT = Annotated[
    EntityCreatedAt | int,
    Field(description="The Entity Created At field"),
    AfterValidator(validate_datetime_value_object),
]
FIELD_ENTITY_ID = Annotated[
    EntityId | str,
    Field(description="The Entity Created At field"),
    AfterValidator(validate_str_value_object),
]


# endregion-------------------------------------------------------------------------
