# endregion-------------------------------------------------------------------------
# region INFRASTRUCTURE DISPATCHERS EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from ..exceptions import InfrastructureExceptionBase


@dataclass(frozen=False)
class InfrastructureDispatcherNoQueryHandlerFound(InfrastructureExceptionBase):
    name: str

    @property
    def message(self) -> str:
        return "There is no query handler for query {self.name}"


@dataclass(frozen=False)
class InfrastructureDispatcherNoCommandHandlerFound(InfrastructureExceptionBase):
    name: str

    @property
    def message(self) -> str:
        return "There are no command handlers for command {self.name}"


@dataclass(frozen=False)
class InfrastructureDispatcherNoEventHandlerFound(InfrastructureExceptionBase):
    name: str

    @property
    def message(self) -> str:
        return "There are no event handlers for event {self.name}"


# endregion-------------------------------------------------------------------------
