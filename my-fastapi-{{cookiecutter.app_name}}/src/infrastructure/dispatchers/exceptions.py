# endregion-------------------------------------------------------------------------
# region DISPATCHER EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from ..exceptions import InfrastructureExceptionBase

@dataclass(frozen=False)
class DispatcherNoQueryHandlerFound(InfrastructureExceptionBase):
    name: str

    @property
    def message(self) -> str:
        return f"There is no query handler for query {self.name}"


@dataclass(frozen=False)
class DispatcherNoCommandHandlerFound(InfrastructureExceptionBase):
    name: str

    @property
    def message(self) -> str:
        return f"There are no command handlers for command {self.name}"


@dataclass(frozen=False)
class DispatcherNoEventHandlerFound(InfrastructureExceptionBase):
    name: str

    @property
    def message(self) -> str:
        return f"There are no event handlers for event {self.name}"


# endregion-------------------------------------------------------------------------
