# endregion-------------------------------------------------------------------------
# region CONFIG
# ----------------------------------------------------------------------------------
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    APP_PORT: Annotated[int, Field(alias="APP_PORT")] = 8000

    LOGGER_CONFIG_PATH: Annotated[str, Field(alias="LOGGER_CONFIG_PATH")] = (
        "logger.yaml"
    )


# endregion-------------------------------------------------------------------------
