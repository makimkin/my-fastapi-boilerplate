# endregion-------------------------------------------------------------------------
# region API VALIDATORS
# ----------------------------------------------------------------------------------
from domain.common.value_object import ValueObjectBase


def validate_value_object[T](value_object: ValueObjectBase[T] | str) -> T | str:
    if isinstance(value_object, str):
        return value_object

    return value_object.as_raw()


# endregion-------------------------------------------------------------------------
