# endregion-------------------------------------------------------------------------
# region BASE VALUE OBJECTS
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ValueObjectBase[T: Any](ABC):
    value: T

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self): ...

    @abstractmethod
    def as_raw(self) -> T: ...


# endregion-------------------------------------------------------------------------
