# endregion-------------------------------------------------------------------------
# region CONFIG
# ----------------------------------------------------------------------------------
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=".env",
        extra="ignore",
    )

    APP_PORT: Annotated[int, Field(alias="APP_PORT")] = 8000

    LOGGER_CONFIG_PATH: Annotated[str, Field(alias="LOGGER_CONFIG_PATH")] = (
        "logger.yaml"
    )

    MONGO_HOST: Annotated[str, Field(alias="MONGO_HOST")] = "localhost"
    MONGO_PORT: Annotated[int, Field(alias="MONGO_PORT")] = 27017
    MONGO_DB: Annotated[str, Field(alias="MONGO_DB")] = "db"

    SQL_HOST: Annotated[str, Field(alias="SQL_HOST")] = "localhost"
    SQL_USER: Annotated[str, Field(alias="SQL_USER")] = "user"
    SQL_PASS: Annotated[str, Field(alias="SQL_PASS")] = "pass"
    SQL_PORT: Annotated[int, Field(alias="SQL_PORT")] = 5432
    SQL_DB: Annotated[str, Field(alias="SQL_DB")] = "db"

    KAFKA_PORT: Annotated[int, Field(alias="KAFKA_PORT")] = 9092
    KAFKA_HOST: Annotated[str, Field(alias="KAFKA_HOST")] = "broker"

    REDIS_HOST: Annotated[str, Field(alias="REDIS_HOST")] = "localhost"
    REDIS_PORT: Annotated[int, Field(alias="REDIS_PORT")] = 6379

    TOPIC_NAME_PRODUCT_CREATED: Annotated[
        str,
        Field(alias="TOPIC_NAME_PRODUCT_CREATED"),
    ] = "product_createddd"

    @property
    def MONGO_URI(self) -> str:
        return f"mongodb://{self.MONGO_HOST}:{self.MONGO_PORT}/{self.MONGO_DB}"

    @property
    def SQL_URI(self) -> str:
        return f"postgresql+asyncpg://{self.SQL_USER}:{self.SQL_PASS}@{self.SQL_HOST}:{self.SQL_PORT}/{self.SQL_DB}"

    @property
    def KAFKA_URI(self) -> str:
        return f"{self.KAFKA_HOST}:{self.KAFKA_PORT}"

    @property
    def REDIS_URI(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


# endregion-------------------------------------------------------------------------
