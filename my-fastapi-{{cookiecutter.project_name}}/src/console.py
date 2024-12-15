# endregion-------------------------------------------------------------------------
# region APPLICATION CONSOLE
# ----------------------------------------------------------------------------------
import logging

from settings.config import Config

import httpx
import typer
import uvicorn

console = typer.Typer()

logger = logging.getLogger(__name__)


# endregion-------------------------------------------------------------------------
# region CHECK HEALTH
# ----------------------------------------------------------------------------------
@console.command()
def check_health():
    config = Config()

    with httpx.Client() as client:
        response = client.get(f"http://0.0.0.0:{config.APP_PORT}/check/health")
        response.raise_for_status()


# endregion-------------------------------------------------------------------------
# region RUN
# ----------------------------------------------------------------------------------
@console.command()
def run():
    config = Config()
    uvicorn.run(
        "application.api.main:create_app",
        reload=True,
        factory=True,
        host="0.0.0.0",  # noqa: S104
        port=config.APP_PORT,
    )


if __name__ == "__main__":
    console()


# endregion-------------------------------------------------------------------------
