# endregion-------------------------------------------------------------------------
# region BASE SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated

from ..schemas import APISchema

from pydantic import Field


# endregion-------------------------------------------------------------------------
# region HEALTHCHECK
# ----------------------------------------------------------------------------------
class BaseHealthCheckResponse(APISchema):
    di: Annotated[str, Field(alias="di")]


# endregion-------------------------------------------------------------------------
