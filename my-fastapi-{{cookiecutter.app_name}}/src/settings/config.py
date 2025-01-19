# endregion-------------------------------------------------------------------------
# region CONFIG
# ----------------------------------------------------------------------------------
from typing import Annotated, Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=".env",
        extra="ignore",
    )
    # fmt: off
    APP_PORT: Annotated[int, Field(alias="APP_PORT")] = 8000
    APP_DB: Annotated[Literal["mongo", "postgres"], Field(alias="APP_DB")] = "mongo"

    LOGGER_CONFIG_PATH: Annotated[str, Field(alias="LOGGER_CONFIG_PATH")] = "logger.yaml"

    AUTH_ACCESS_TOKEN_SECRET_KEY: Annotated[str, Field(alias="AUTH_ACCESS_TOKEN_SECRET_KEY")] = ""
    AUTH_ACCESS_TOKEN_EXPIRATION_SECONDS: Annotated[int, Field(alias="AUTH_ACCESS_TOKEN_EXPIRATION_SECONDS")] = 60 * 15 # 15 minutes

    AUTH_REFRESH_TOKEN_SECRET_KEY: Annotated[str, Field(alias="AUTH_REFRESH_TOKEN_SECRET_KEY")] = ""
    AUTH_REFRESH_TOKEN_EXPIRATION_SECONDS: Annotated[int, Field(alias="AUTH_REFRESH_TOKEN_EXPIRATION_SECONDS")] = 60 * 60 * 24 * 7 # 7 days

    MONGO_HOST: Annotated[str, Field(alias="MONGO_HOST")] = "localhost"
    MONGO_PORT: Annotated[int, Field(alias="MONGO_PORT")] = 27017
    MONGO_DB: Annotated[str, Field(alias="MONGO_DB")] = "db"

    POSTGRES_HOST: Annotated[str, Field(alias="POSTGRES_HOST")] = "localhost"
    POSTGRES_USER: Annotated[str, Field(alias="POSTGRES_USER")] = "user"
    POSTGRES_PASS: Annotated[str, Field(alias="POSTGRES_PASS")] = "pass"  # noqa: S105
    POSTGRES_PORT: Annotated[int, Field(alias="POSTGRES_PORT")] = 5432
    POSTGRES_DB: Annotated[str, Field(alias="POSTGRES_DB")] = "db"

    KAFKA_PORT: Annotated[int, Field(alias="KAFKA_PORT")] = 9092
    KAFKA_HOST: Annotated[str, Field(alias="KAFKA_HOST")] = "broker"

    REDIS_HOST: Annotated[str, Field(alias="REDIS_HOST")] = "localhost"
    REDIS_PORT: Annotated[int, Field(alias="REDIS_PORT")] = 6379
    # fmt: on

    @property
    def MONGO_URI(self) -> str:
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB}"

    @property
    def SQL_URI(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def KAFKA_URI(self) -> str:
        return f"{self.KAFKA_HOST}:{self.KAFKA_PORT}"

    @property
    def REDIS_URI(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


# endregion-------------------------------------------------------------------------
