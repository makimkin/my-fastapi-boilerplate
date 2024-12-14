# endregion-------------------------------------------------------------------------
# region MESSAGE HANDLERS
# ----------------------------------------------------------------------------------
from fastapi.routing import APIRouter
from fastapi import status

from application.api.schemas import ErrorSchema

from .base import BASE_ACTIONS, PREFIX


from .schemas import BaseHealthCheckResponse

router = APIRouter(prefix=PREFIX)


@router.post(
    BASE_ACTIONS.HEALTHCHECK,
    response_model=BaseHealthCheckResponse,
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema}},
)
async def base_healthcheck() -> dict:
    """-----------------------------------------------------------------------------
    The Base Healthcheck Handler.
    -----------------------------------------------------------------------------"""
    return dict(message="✅")


# endregion-------------------------------------------------------------------------
