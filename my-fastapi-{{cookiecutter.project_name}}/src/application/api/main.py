# endregion-------------------------------------------------------------------------
# region MAIN
# ----------------------------------------------------------------------------------
from contextlib import asynccontextmanager

from infrastructure.di.app import DIProviderApp
from application.api.lifespan import on_startup, on_shutdown
from application.api.base.router import router as base_router

from dishka import make_async_container
from fastapi import FastAPI
from dishka.integrations.fastapi import setup_dishka

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

    container = make_async_container(DIProviderApp())
    setup_dishka(container=container, app=app)

    return app


def create_app() -> FastAPI:
    app = create_app_base()

    return app


# endregion-------------------------------------------------------------------------
