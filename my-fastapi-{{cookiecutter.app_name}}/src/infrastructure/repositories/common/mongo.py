# endregion-------------------------------------------------------------------------
# region MONGO REPOSITORY
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from motor.motor_asyncio import AsyncIOMotorCollection

from domain.common.entity import EntityBase

from .base import RepositoryBase


@dataclass
class RepositoryMongo[E: EntityBase](RepositoryBase, ABC):
    collection: AsyncIOMotorCollection

    @abstractmethod
    def to_domain(self, document: dict) -> E: ...

    @abstractmethod
    def to_document(self, entity: E) -> dict: ...


# endregion-------------------------------------------------------------------------
