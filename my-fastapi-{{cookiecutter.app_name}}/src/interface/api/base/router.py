# endregion-------------------------------------------------------------------------
# region BASE HANDLERS
# ----------------------------------------------------------------------------------
from fastapi.routing import APIRouter
from fastapi import status

from infrastructure.connection_manager.common.base import ConnectionManagerBase
from infrastructure.authenticator.base import AuthenticatorBase

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from .base import BASE_PREFIX, BASE_TAG, BASE_ACTIONS
from .schemas import BaseHealthCheckResponse

router = APIRouter(
    prefix=BASE_PREFIX,
    route_class=DishkaRoute,
    tags=[BASE_TAG],
)


@router.get(
    BASE_ACTIONS.HEALTHCHECK,
    status_code=status.HTTP_200_OK,
    response_model=BaseHealthCheckResponse,
)
async def base_health_check(
    connection_manager: FromDishka[ConnectionManagerBase],
    authenticator: FromDishka[AuthenticatorBase],
) -> dict:
    """-----------------------------------------------------------------------------
    The Base Health Check Handler.
    -----------------------------------------------------------------------------"""
    return {
        "authenticator": {
            "name": authenticator.__class__.__name__,
            "health": "✅" if await authenticator.check_health() else "❌",
        },
        "connection_manager": {
            "name": connection_manager.__class__.__name__,
            "health": "✅" if await connection_manager.check_health() else "❌",
        },
    }


# endregion-------------------------------------------------------------------------
