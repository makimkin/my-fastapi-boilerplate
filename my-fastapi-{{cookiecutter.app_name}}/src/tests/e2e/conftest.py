# endregion-------------------------------------------------------------------------
# region CONFTEST
# ----------------------------------------------------------------------------------
import pytest_asyncio
import pytest

from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container

from dataclasses import dataclass
from fastapi import FastAPI
from typing import Any

from infrastructure.containers.mock import ContainerMock

from httpx import ASGITransport, Response, AsyncClient

from application.api.main import create_app_mock


# endregion-------------------------------------------------------------------------
# region CONTEXT TEST
# ----------------------------------------------------------------------------------
@dataclass
class ContextTest:
    app: FastAPI
    client: AsyncClient

    async def post(
        self,
        url: str,
        json: Any | None = None,
        **kwargs,
    ) -> Response:
        return await self.client.post(
            url=url,
            json=json,
            **kwargs,
        )

    async def get(
        self,
        url: str,
        **kwargs,
    ) -> Response:
        return await self.client.get(
            url=url,
            **kwargs,
        )


# endregion-------------------------------------------------------------------------
# region FIXTURES
# ----------------------------------------------------------------------------------
@pytest_asyncio.fixture
async def container():
    container = make_async_container(ContainerMock())
    yield container
    await container.close()


@pytest.fixture(scope="function")
def app(container) -> FastAPI:
    app = create_app_mock()
    setup_dishka(container, app)

    return app


@pytest.fixture(scope="function")
def transport(app: FastAPI) -> ASGITransport:
    return ASGITransport(app=app)


@pytest_asyncio.fixture(scope="function")
async def client(transport: ASGITransport):
    async with AsyncClient(
        transport=transport,
        base_url="http://testserver",
        follow_redirects=True,
    ) as client:
        yield client


@pytest_asyncio.fixture(scope="function")
def context(app: FastAPI, client: AsyncClient) -> ContextTest:
    return ContextTest(app=app, client=client)


# endregion-------------------------------------------------------------------------
