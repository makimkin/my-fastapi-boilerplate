# endregion-------------------------------------------------------------------------
# region SQL REPOSITORY
# ----------------------------------------------------------------------------------
from dataclasses import dataclass
from abc import ABC

from .base import RepositoryBase

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


@dataclass
class RepositorySQL(RepositoryBase, ABC):
    session_maker: async_sessionmaker[AsyncSession]


# endregion-------------------------------------------------------------------------
