# endregion-------------------------------------------------------------------------
# region MAIN
# ----------------------------------------------------------------------------------
import logging

from contextlib import asynccontextmanager

from .exception_handlers import base_exception_handler
from .lifespan import on_startup, on_shutdown
from .base import base_router

from domain.common.exceptions import ExceptionBase

from infrastructure.containers.app import ContainerApp

from logger import setup_logger

from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container

from fastapi import APIRouter, FastAPI

logger = logging.getLogger("app")


router_v1 = APIRouter(prefix="/v1")


@asynccontextmanager
async def lifespan_manager(app: FastAPI):
    await on_startup(app)

    yield

    await on_shutdown(app)


def create_app_base() -> FastAPI:
    app = FastAPI(
        title="KOT API",
        lifespan=lifespan_manager,
        description="API for kot",
        version="0.1.0",
    )

    router_v1.include_router(base_router)

    app.include_router(router_v1)

    app.exception_handlers[ExceptionBase] = base_exception_handler

    return app


def create_app() -> FastAPI:
    app = create_app_base()

    container = make_async_container(ContainerApp())
    setup_dishka(container=container, app=app)
    setup_logger(default_level=logging.INFO)

    return app


def create_app_mock() -> FastAPI:
    return create_app_base()


# endregion-------------------------------------------------------------------------
