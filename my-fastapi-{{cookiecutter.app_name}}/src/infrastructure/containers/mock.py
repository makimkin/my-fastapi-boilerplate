# endregion-------------------------------------------------------------------------
# region CONTAINER MOCK
# ----------------------------------------------------------------------------------
from .repositories.memory import MemoryRepositoriesContainer
from .cache.memory import MemoryCacheContainer
from .base import ContainerBase


class ContainerMock(
    ContainerBase,
    MemoryCacheContainer,
    MemoryRepositoriesContainer,
): ...


# endregion-------------------------------------------------------------------------
