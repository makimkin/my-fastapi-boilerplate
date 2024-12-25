# endregion-------------------------------------------------------------------------
# region BASE HANDLERS
# ----------------------------------------------------------------------------------
from settings.config import Config

from fastapi.routing import APIRouter
from fastapi import status

from dishka.integrations.fastapi import FromDishka, DishkaRoute

from .base import PREFIX, BASE_ACTIONS
from .schemas import BaseHealthCheckResponse

router = APIRouter(prefix=PREFIX, route_class=DishkaRoute)


@router.get(
    BASE_ACTIONS.HEALTHCHECK,
    status_code=status.HTTP_200_OK,
    response_model=BaseHealthCheckResponse,
)
async def base_health_check(config: FromDishka[Config]) -> dict:
    """-----------------------------------------------------------------------------
    The Base Health Check Handler.
    -----------------------------------------------------------------------------"""
    return {"di": "✅" if config is not None else "❌"}


# endregion-------------------------------------------------------------------------
