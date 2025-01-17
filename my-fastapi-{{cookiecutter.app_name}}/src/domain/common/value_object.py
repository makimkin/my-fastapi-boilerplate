# endregion-------------------------------------------------------------------------
# region BASE VALUE OBJECTS
# ----------------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass
from uuid import UUID, uuid4

from ..exceptions import ValueObjectEntityIdIncorrectValueException


@dataclass(frozen=True)
class ValueObjectBase[V](ABC):
    _value: V

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self): ...

    @abstractmethod
    def as_raw(self) -> V: ...


@dataclass(frozen=True)
class EntityId(ValueObjectBase[str]):
    def validate(self):
        try:
            UUID(self._value)
        except (ValueError, TypeError) as e:
            raise ValueObjectEntityIdIncorrectValueException(value=self._value) from e

    @classmethod
    def create(cls) -> "EntityId":
        return EntityId(_value=str(uuid4()))

    def as_raw(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self.as_raw()


# endregion-------------------------------------------------------------------------
