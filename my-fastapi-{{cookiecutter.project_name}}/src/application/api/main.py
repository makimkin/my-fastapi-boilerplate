# endregion-------------------------------------------------------------------------
# region MAIN
# ----------------------------------------------------------------------------------
import logging

from contextlib import asynccontextmanager

from application.api.exception_handlers import base_exception_handler
from application.api.base.router import router as base_router
from application.api.lifespan import on_startup, on_shutdown
from application.exceptions import BaseApplicationException

from infrastructure.containers.app import ContainerApp

from logger import setup_logger

from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container

from fastapi import FastAPI

logger = logging.getLogger("app")


@asynccontextmanager
async def lifespan_manager(app: FastAPI):
    await on_startup()

    yield

    await on_shutdown(app)


def create_app_base() -> FastAPI:
    app = FastAPI(
        title="{{cookiecutter.app_name.upper()}} API",
        lifespan=lifespan_manager,
        description="API for {{cookiecutter.app_name}}",
        version="0.1.0",
    )
    app.include_router(base_router)

    app.exception_handlers[BaseApplicationException] = base_exception_handler

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
