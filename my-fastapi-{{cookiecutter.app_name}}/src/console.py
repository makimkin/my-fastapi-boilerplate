# endregion-------------------------------------------------------------------------
# region APPLICATION CONSOLE
# ----------------------------------------------------------------------------------
from settings.config import Config

import httpx
import typer
import uvicorn

console = typer.Typer()


# endregion-------------------------------------------------------------------------
# region CHECK HEALTH
# ----------------------------------------------------------------------------------
@console.command()
def check_health():
    config = Config()

    with httpx.Client() as client:
        response = client.get(f"http://0.0.0.0:{config.APP_PORT}/v1/check/health")
        response.raise_for_status()


# endregion-------------------------------------------------------------------------
# region RUN
# ----------------------------------------------------------------------------------
@console.command()
def run():
    config = Config()
    uvicorn.run(
        "interface.api.main:create_app",
        reload=True,
        factory=True,
        host="0.0.0.0",  # noqa: S104
        port=config.APP_PORT,
    )


if __name__ == "__main__":
    console()


# endregion-------------------------------------------------------------------------
