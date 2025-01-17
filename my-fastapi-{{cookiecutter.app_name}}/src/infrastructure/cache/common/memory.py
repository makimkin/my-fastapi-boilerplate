# endregion-------------------------------------------------------------------------
# region MEMORY CACHE
# ----------------------------------------------------------------------------------
import datetime
import orjson
import re

from dataclasses import dataclass, field
from typing import Any
from abc import ABC

from .base import CacheBase


@dataclass
class CacheMemory(CacheBase, ABC):
    _saved: dict[str, bytes] = field(default_factory=dict)
    _expiration_timestamps: dict[str, datetime.datetime] = field(default_factory=dict)

    @staticmethod
    def _apply_expiration(func):
        async def wrapper(self: "CacheMemory", *args, **kwargs):
            self._delete_expired()

            return await func(self, *args, **kwargs)

        return wrapper

    @_apply_expiration
    async def get(self, key: str) -> Any | None:
        value = self._saved.get(key, None)

        if value is None:
            return None

        return orjson.loads(value)

    @_apply_expiration
    async def set(
        self,
        key: str,
        value: Any,
        *,
        expiration_milliseconds: int | None = None,
    ) -> None:
        self._saved[key] = orjson.dumps(value)

        if expiration_milliseconds is not None:
            self._expiration_timestamps[key] = (
                datetime.datetime.now()
                + datetime.timedelta(milliseconds=expiration_milliseconds)
            )

    @_apply_expiration
    async def get_keys(self, pattern: str) -> list[str]:
        p = re.compile(pattern.replace("*", ".*"))

        return [key for key in self._saved.keys() if p.match(key)]

    @_apply_expiration
    async def get_values(
        self,
        keys: list[str],
        _: int = 100,
    ) -> dict[str, Any | None]:
        return {
            key: orjson.loads(self._saved[key]) if key in self._saved else None
            for key in keys
        }

    def _delete_expired(self):
        keys = []

        for key, expiration in self._expiration_timestamps.items():
            if expiration < datetime.datetime.now():
                keys.append(key)

        for key in keys:
            del self._expiration_timestamps[key]
            del self._saved[key]


# endregion-------------------------------------------------------------------------
