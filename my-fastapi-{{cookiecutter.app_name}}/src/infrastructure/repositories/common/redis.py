# endregion-------------------------------------------------------------------------
# region REDIS REPOSITORY
# ----------------------------------------------------------------------------------
import aioredis

from dataclasses import dataclass
from abc import ABC

from .base import RepositoryBase


@dataclass
class RepositoryRedis(RepositoryBase, ABC):
    redis: aioredis.Redis


# endregion-------------------------------------------------------------------------
