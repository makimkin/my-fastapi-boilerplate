# endregion-------------------------------------------------------------------------
# region CONFIG
# ----------------------------------------------------------------------------------
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


# endregion-------------------------------------------------------------------------
