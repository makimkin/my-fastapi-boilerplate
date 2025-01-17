# endregion-------------------------------------------------------------------------
# region LIFESPAN MANAGER
# ----------------------------------------------------------------------------------
import logging

from dataclasses import dataclass

from dishka import AsyncContainer
from fastapi import FastAPI

logger = logging.getLogger("app")


@dataclass
class LifespanManager:
    app: FastAPI

    @property
    def container(self) -> AsyncContainer:
        return self.app.state.dishka_container

    async def __aenter__(self) -> None:
        """-----------------------------------------------------------------------------
        Activate the lifespan of the application.
        -----------------------------------------------------------------------------"""
        logger.info("STARTUP")

    async def __aexit__(self, *_, **__) -> None:
        """-----------------------------------------------------------------------------
        Deactivate the lifespan of the application.
        -----------------------------------------------------------------------------"""
        logger.info("SHUTDOWN")

        await self.container.close()


# endregion-------------------------------------------------------------------------
