# endregion-------------------------------------------------------------------------
# region BASE SCHEMAS
# ----------------------------------------------------------------------------------
from pydantic import Field

from typing import Annotated

from application.api.schemas import ParentSchema


# endregion-------------------------------------------------------------------------
# region HEALTHCHECK
# ----------------------------------------------------------------------------------
class BaseHealthCheckResponse(ParentSchema):
    di: Annotated[str, Field(alias="di")]


# endregion-------------------------------------------------------------------------
