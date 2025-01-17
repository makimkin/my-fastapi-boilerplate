# endregion-------------------------------------------------------------------------
# region CONTAINER APP
# ----------------------------------------------------------------------------------
from .base import ContainerBase
from .cache.redis import RedisCacheContainer
from .repositories.sql import SQLRepositoriesContainer


class ContainerApp(
    ContainerBase,
    RedisCacheContainer,
    SQLRepositoriesContainer,
): ...


# endregion-------------------------------------------------------------------------
