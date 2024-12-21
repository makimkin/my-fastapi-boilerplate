# endregion-------------------------------------------------------------------------
# region LIFE SPAN CALLBACKS
# ----------------------------------------------------------------------------------
import logging

from fastapi import FastAPI

from infrastructure.producers.base import ProducerBase

logger = logging.getLogger("app")


async def on_startup(app: FastAPI) -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application startup.
    -----------------------------------------------------------------------------"""
    logger.info("STARTUP")

    producer = await app.state.dishka_container.get(ProducerBase)
    await producer.connect()


async def on_shutdown(app: FastAPI) -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application shutdown.
    -----------------------------------------------------------------------------"""
    logger.info("SHUTDOWN")

    producer = await app.state.dishka_container.get(ProducerBase)
    await producer.close()

    await app.state.dishka_container.close()


# endregion-------------------------------------------------------------------------
