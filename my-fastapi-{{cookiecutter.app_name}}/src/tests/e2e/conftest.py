# endregion-------------------------------------------------------------------------
# region CONFTEST
# ----------------------------------------------------------------------------------
import pytest_asyncio
import pytest

from dishka.integrations.fastapi import setup_dishka
from dishka import AsyncContainer, make_async_container

from dataclasses import dataclass
from fastapi import FastAPI
from typing import Any, AsyncIterable

from infrastructure.containers.mock import ContainerMock

from httpx import ASGITransport, Response, AsyncClient

from interface.api.main import create_app_mock

from settings.config import Config


# endregion-------------------------------------------------------------------------
# region CONTEXT TEST
# ----------------------------------------------------------------------------------
@dataclass
class ContextTest:
    app: FastAPI
    client: AsyncClient
    config: Config

    async def post(
        self,
        url: str,
        json: Any | None = None,
        data: Any | None = None,
        params: dict[str, Any] | None = None,
        access_token: str | None = None,
        **kwargs,
    ) -> Response:
        headers = self.get_headers(access_token=access_token)

        return await self.client.post(
            url=url,
            json=json,
            data=data,
            params=params,
            headers=headers,
            **kwargs,
        )

    async def patch(
        self,
        url: str,
        json: Any | None = None,
        data: Any | None = None,
        access_token: str | None = None,
        **kwargs,
    ) -> Response:
        headers = self.get_headers(access_token=access_token)

        return await self.client.patch(
            url=url,
            json=json,
            data=data,
            headers=headers,
            **kwargs,
        )

    async def get(
        self,
        url: str,
        access_token: str | None = None,
        params: dict[str, Any] | None = None,
        **kwargs,
    ) -> Response:
        headers = self.get_headers(access_token=access_token)

        return await self.client.get(
            url=url,
            params=params,
            headers=headers,
            **kwargs,
        )

    def get_headers(self, access_token: str | None = None) -> dict[str, str]:
        headers = {}

        if access_token is not None:
            headers["Authorization"] = f"Bearer {access_token}"

        return headers


# endregion-------------------------------------------------------------------------
# region FIXTURES
# ----------------------------------------------------------------------------------
@pytest_asyncio.fixture
async def container() -> AsyncIterable[AsyncContainer]:
    container = make_async_container(ContainerMock())
    yield container
    await container.close()


@pytest.fixture(scope="function")
def app(container: AsyncContainer) -> FastAPI:
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
async def config(container) -> Config:
    return await container.get(Config)


@pytest_asyncio.fixture(scope="function")
def context(
    app: FastAPI,
    client: AsyncClient,
    config: Config,
) -> ContextTest:
    return ContextTest(app=app, client=client, config=config)


# endregion-------------------------------------------------------------------------
