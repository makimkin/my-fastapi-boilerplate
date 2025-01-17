# endregion-------------------------------------------------------------------------
# region REDIS CACHE
# ----------------------------------------------------------------------------------
import logging
import orjson

from dataclasses import dataclass
from typing import Any
from abc import ABC

from redis.asyncio.client import Redis

from .base import CacheBase

logger = logging.getLogger("app")


@dataclass
class CacheRedis(CacheBase, ABC):
    redis: Redis

    async def get(self, key: str) -> Any | None:
        value = await self.redis.get(key)

        if value is None:
            return None

        return orjson.loads(value)

    async def set(
        self,
        key: str,
        value: Any,
        *,
        expiration_milliseconds: int | None = None,
    ) -> None:
        await self.redis.set(
            key,
            orjson.dumps(value),
            px=expiration_milliseconds,
        )

    async def get_keys(self, pattern: str) -> list[str]:
        cursor, keys = 0, []

        while True:
            try:
                cursor, partial_keys = await self.redis.scan(
                    cursor=cursor,
                    match=pattern,
                    count=100,
                )

                keys.extend(partial_keys)

                if cursor == 0:
                    break

            except Exception as e:
                logger.error("Error while scanning keys", exc_info=e)
                break

        return keys

    async def get_values(
        self,
        keys: list[str],
        batch_size: int = 100,
    ) -> dict[str, Any | None]:
        values = {}

        for i in range(0, len(keys), batch_size):
            partial_keys = keys[i : i + batch_size]

            partial_values = await self.redis.mget(*partial_keys)

            for key, value in zip(partial_keys, partial_values, strict=False):
                values[key] = orjson.loads(value) if value is not None else None

        return values


# endregion-------------------------------------------------------------------------
