# endregion-------------------------------------------------------------------------
# region MAIN
# ----------------------------------------------------------------------------------
import logging

from contextlib import asynccontextmanager

from application.api.base.router import router as base_router
from application.api.lifespan import on_startup, on_shutdown

from infrastructure.di.app import DIProviderApp

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
    logger.info("App created")

    app.include_router(base_router)

    return app


def create_app() -> FastAPI:
    app = create_app_base()

    container = make_async_container(DIProviderApp())
    setup_dishka(container=container, app=app)
    logger.info("DI container set up")

    setup_logger(default_level=logging.INFO)

    return app


# endregion-------------------------------------------------------------------------
