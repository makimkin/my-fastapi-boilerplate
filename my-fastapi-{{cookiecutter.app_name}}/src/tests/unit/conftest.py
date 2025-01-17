# endregion-------------------------------------------------------------------------
# region CONFTEST
# ----------------------------------------------------------------------------------
import pytest_asyncio
import pytest

from dishka import AsyncContainer, make_async_container

from infrastructure.producers.common.base import ProducerBase
from infrastructure.dispatchers.dispatcher import Dispatcher
from infrastructure.containers.mock import ContainerMock

from settings.config import Config


@pytest.fixture(scope="function")
def container() -> AsyncContainer:
    return make_async_container(ContainerMock())


@pytest_asyncio.fixture(scope="function")
async def dispatcher(container: AsyncContainer) -> Dispatcher:
    return await container.get(Dispatcher)


@pytest_asyncio.fixture(scope="function")
async def producer(container: AsyncContainer) -> ProducerBase:
    return await container.get(ProducerBase)


@pytest_asyncio.fixture(scope="function")
async def config(container: AsyncContainer) -> Config:
    return await container.get(Config)


# endregion-------------------------------------------------------------------------
