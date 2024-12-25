# endregion-------------------------------------------------------------------------
# region LIFE SPAN CALLBACKS
# ----------------------------------------------------------------------------------
import logging

from fastapi import FastAPI

from infrastructure.producers.base import ProducerBase

from dishka.exceptions import NoFactoryError

logger = logging.getLogger("app")


async def on_startup(app: FastAPI) -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application startup.
    -----------------------------------------------------------------------------"""
    logger.info("STARTUP")

    try:
        logger.info("Connecting to producer")
        producer = await app.state.dishka_container.get(ProducerBase)
        await producer.connect()
        logger.info("Connected to producer")
    except NoFactoryError as e:
        logger.error("No factory found for producer", exc_info=e)


async def on_shutdown(app: FastAPI) -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application shutdown.
    -----------------------------------------------------------------------------"""
    logger.info("SHUTDOWN")

    try:
        logger.info("Closing producer")
        producer = await app.state.dishka_container.get(ProducerBase)
        await producer.close()
        logger.info("Closed producer")
    except NoFactoryError as e:
        logger.error("No factory found for producer", exc_info=e)

    await app.state.dishka_container.close()


# endregion-------------------------------------------------------------------------
