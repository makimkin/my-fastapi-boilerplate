# endregion-------------------------------------------------------------------------
# region LIFE SPAN CALLBACKS
# ----------------------------------------------------------------------------------
import logging

from fastapi import FastAPI


logger = logging.getLogger(__name__)


async def on_startup() -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application startup.
    -----------------------------------------------------------------------------"""
    logger.info("STARTUP:\tBase Broker is Connected")


async def on_shutdown(app: FastAPI) -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application shutdown.
    -----------------------------------------------------------------------------"""
    logger.info("SHUTDOWN:\tBase Broker is Closed")

    await app.state.dishka_container.close()


# endregion-------------------------------------------------------------------------
