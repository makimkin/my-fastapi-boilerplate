# endregion-------------------------------------------------------------------------
# region HEALTH CHECK TESTS
# ----------------------------------------------------------------------------------
import pytest

from fastapi import status
from faker import Faker

from interface.api.base.base import BASE_ACTIONS, BASE_PREFIX
from interface.api.base.schemas import (
    BaseHealthCheckResponse,
)

from .conftest import ContextTest


@pytest.mark.asyncio
async def test_health_check_success(
    context: ContextTest,
    faker: Faker,
) -> None:
    """-----------------------------------------------------------------------------
    Test health check success.
    -----------------------------------------------------------------------------"""
    # fmt: off
    health_check_response = await context.get(f"/v1{BASE_PREFIX}{BASE_ACTIONS.HEALTHCHECK}")
    assert health_check_response.status_code == status.HTTP_200_OK, health_check_response.text

    health_check_json, text = health_check_response.json(), health_check_response.text
    assert "producer" in health_check_json, text
    assert "authenticator" in health_check_json, text
    assert "connectionManager" in health_check_json, text

    health_check_data = BaseHealthCheckResponse(**health_check_json)
    assert health_check_data.producer is not None, text
    assert health_check_data.authenticator is not None, text
    assert health_check_data.connection_manager is not None, text
    # fmt: on


# endregion-------------------------------------------------------------------------
