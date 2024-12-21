# endregion-------------------------------------------------------------------------
# region MONGO REPOSITORY
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

from motor.core import AgnosticClient

from .base import RepositoryBase


@dataclass
class RepositoryMongo(RepositoryBase, ABC):
    mongo_client: AgnosticClient
    mongo_db_name: str

    @property
    def collection(self):
        return self.mongo_client[self.mongo_db_name][self.mongo_collection_name]

    @property
    def mongo_collection_name(self) -> str:
        return self._get_mongo_collection_name()

    @classmethod
    @abstractmethod
    def _get_mongo_collection_name(cls) -> str: ...


# endregion-------------------------------------------------------------------------
