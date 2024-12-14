# endregion-------------------------------------------------------------------------
# region BASE SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from application.api.schemas import ParentSchema

from pydantic import Field

# endregion-------------------------------------------------------------------------
# region HEALTHCHECK
# ----------------------------------------------------------------------------------
class BaseHealthCheckResponse(ParentSchema):
    di: Annotated[str, Field(alias="di")]


# endregion-------------------------------------------------------------------------
