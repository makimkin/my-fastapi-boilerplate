# endregion-------------------------------------------------------------------------
# region MAIN
# ----------------------------------------------------------------------------------
from contextlib import asynccontextmanager
from fastapi import FastAPI

from application.api.base.router import router as base_router
from application.api.lifespan import on_shutdown, on_startup


@asynccontextmanager
async def lifespan_manager(app: FastAPI):
    await on_startup()

    yield

    await on_shutdown(app)


def create_app_base() -> FastAPI:
    app = FastAPI(
        title="{{cookiecutter.app_name}} API",
        lifespan=lifespan_manager,
        description="API for {{cookiecutter.app_name}}",
        version="0.1.0",
    )

    app.include_router(base_router)

    return app


def create_app() -> FastAPI:
    app = create_app_base()

    return app


# endregion-------------------------------------------------------------------------
