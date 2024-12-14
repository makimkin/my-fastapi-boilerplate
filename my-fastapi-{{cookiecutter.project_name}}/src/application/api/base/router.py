# endregion-------------------------------------------------------------------------
# region MESSAGE HANDLERS
# ----------------------------------------------------------------------------------
from dishka.integrations.fastapi import DishkaRoute, FromDishka

from fastapi.routing import APIRouter
from fastapi import status

from application.api.schemas import ErrorSchema

from settings.config import Config

from .base import BASE_ACTIONS, PREFIX
from .schemas import BaseHealthCheckResponse

router = APIRouter(prefix=PREFIX, route_class=DishkaRoute)


@router.get(
    BASE_ACTIONS.HEALTHCHECK,
    response_model=BaseHealthCheckResponse,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema}},
)
async def base_health_check(config: FromDishka[Config]) -> dict:
    """-----------------------------------------------------------------------------
    The Base Healthcheck Handler.
    -----------------------------------------------------------------------------"""
    return dict(di="✅" if config is not None else "❌")


# endregion-------------------------------------------------------------------------
