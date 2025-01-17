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
    authenticator: Annotated[str, Field(alias="authenticator")]
    connection_manager: Annotated[str, Field(alias="connectionManager")]


# endregion-------------------------------------------------------------------------
