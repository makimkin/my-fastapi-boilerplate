# endregion-------------------------------------------------------------------------
# region BASE INFRASTRUCTURE
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class InfrastructureBase(ABC):
    @abstractmethod
    async def check_health(self) -> bool: ...


# endregion-------------------------------------------------------------------------
