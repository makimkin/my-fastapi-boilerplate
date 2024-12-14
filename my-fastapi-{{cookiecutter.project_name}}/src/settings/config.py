# endregion-------------------------------------------------------------------------
# region CONFIG
# ----------------------------------------------------------------------------------
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache(1)
def get_config() -> Config:
    return Config()


# endregion-------------------------------------------------------------------------
