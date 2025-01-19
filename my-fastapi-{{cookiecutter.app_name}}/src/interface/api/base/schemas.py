# endregion-------------------------------------------------------------------------
# region BASE SCHEMAS
# ----------------------------------------------------------------------------------
from typing import Annotated, Literal

from ..schemas import APISchema

from pydantic import Field


# endregion-------------------------------------------------------------------------
# region HEALTHCHECK
# ----------------------------------------------------------------------------------
class BaseHealthCheckResponseStatus(APISchema):
    name: Annotated[str, Field(alias="name")]
    health: Annotated[
        Literal["✅", "❌"],
        Field(alias="health"),
    ]


class BaseHealthCheckResponse(APISchema):
    authenticator: Annotated[
        BaseHealthCheckResponseStatus,
        Field(alias="authenticator"),
    ]
    connection_manager: Annotated[
        BaseHealthCheckResponseStatus,
        Field(alias="connectionManager"),
    ]


# endregion-------------------------------------------------------------------------
