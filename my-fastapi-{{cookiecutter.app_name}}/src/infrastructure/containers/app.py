# endregion-------------------------------------------------------------------------
# region CONTAINER APP
# ----------------------------------------------------------------------------------
from .base import ContainerBase

from settings.config import Config

config = Config()


match config.APP_DB:
    case "mongo":
        from .repositories.mongo import MongoRepositoriesContainer

        ContainerApp = type(
            "ContainerApp",
            (ContainerBase, MongoRepositoriesContainer),
            {},
        )
    case "postgres":
        from .repositories.sql import SQLRepositoriesContainer

        ContainerApp = type(
            "ContainerApp",
            (ContainerBase, SQLRepositoriesContainer),
            {},
        )


# endregion-------------------------------------------------------------------------
