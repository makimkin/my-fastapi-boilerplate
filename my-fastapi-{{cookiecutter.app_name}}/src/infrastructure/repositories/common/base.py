# endregion-------------------------------------------------------------------------
# region BASE REPOSITORY
# ----------------------------------------------------------------------------------
from abc import ABC
from dataclasses import dataclass

from infrastructure.common.base import InfrastructureBase


@dataclass
class RepositoryBase(InfrastructureBase, ABC): ...


# endregion-------------------------------------------------------------------------
