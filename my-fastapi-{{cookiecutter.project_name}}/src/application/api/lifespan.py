# endregion-------------------------------------------------------------------------
# region LIFE SPAN CALLBACKS
# ----------------------------------------------------------------------------------
import logging

from fastapi import FastAPI

logger = logging.getLogger("app")


async def on_startup() -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application startup.
    -----------------------------------------------------------------------------"""
    logger.info("STARTUP")


async def on_shutdown(app: FastAPI) -> None:
    """-----------------------------------------------------------------------------
    Callback to run on application shutdown.
    -----------------------------------------------------------------------------"""
    logger.info("SHUTDOWN")

    await app.state.dishka_container.close()


# endregion-------------------------------------------------------------------------
