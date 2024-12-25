# endregion-------------------------------------------------------------------------
# region SQL REPOSITORY
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from infrastructure.orm.models.base import ModelBase

from domain.common.entity import EntityBase

from .base import RepositoryBase


@dataclass
class RepositorySQL[E: EntityBase, M: ModelBase](RepositoryBase, ABC):
    session_maker: async_sessionmaker[AsyncSession]

    @abstractmethod
    def to_domain(self, model: M) -> E: ...

    @abstractmethod
    def to_model(self, entity: E) -> M: ...


# endregion-------------------------------------------------------------------------
