# endregion-------------------------------------------------------------------------
# region BASE HANDLERS
# ----------------------------------------------------------------------------------
from fastapi.routing import APIRouter
from fastapi import status

from infrastructure.connection_manager.common.base import ConnectionManagerBase
from infrastructure.authenticator.base import AuthenticatorBase
from infrastructure.producers.base import ProducerBase

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from .base import BASE_PREFIX, BASE_ACTIONS
from .schemas import BaseHealthCheckResponse

router = APIRouter(prefix=BASE_PREFIX, route_class=DishkaRoute)


@router.get(
    BASE_ACTIONS.HEALTHCHECK,
    status_code=status.HTTP_200_OK,
    response_model=BaseHealthCheckResponse,
)
async def base_health_check(
    connection_manager: FromDishka[ConnectionManagerBase],
    authenticator: FromDishka[AuthenticatorBase],
    producer: FromDishka[ProducerBase],
) -> dict:
    """-----------------------------------------------------------------------------
    The Base Health Check Handler.
    -----------------------------------------------------------------------------"""
    return {
        "producer": producer.__class__.__name__,
        "authenticator": authenticator.__class__.__name__,
        "connection_manager": connection_manager.__class__.__name__,
    }


# endregion-------------------------------------------------------------------------
