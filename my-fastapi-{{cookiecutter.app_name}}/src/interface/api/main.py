# endregion-------------------------------------------------------------------------
# region MAIN
# ----------------------------------------------------------------------------------
import logging

from .lifespan import LifespanManager

from .exception_handlers import (
    base_exception_handler,
    response_validation_exception_handler,
)

from .base import base_router

from .middlewares import ProcessTimeMiddleware

from exceptions import ExceptionBase

from infrastructure.containers.app import ContainerApp

from logger import setup_logger

from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container

from fastapi.exceptions import ResponseValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, FastAPI

logger = logging.getLogger("app")


router_v1 = APIRouter(prefix="/v1")


allowed_origins = ["http://localhost:5173", "http://localhost:4173"]


def create_app_base() -> FastAPI:
    app = FastAPI(
        title="{{cookiecutter.app_name.upper()}} API",
        lifespan=LifespanManager,
        description="API for {{cookiecutter.app_name}} service",
        version="0.1.0",
    )

    router_v1.include_router(base_router)

    app.include_router(router_v1)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(ProcessTimeMiddleware)

    app.exception_handlers[ExceptionBase] = base_exception_handler
    app.exception_handlers[ResponseValidationError] = (
        response_validation_exception_handler
    )

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
