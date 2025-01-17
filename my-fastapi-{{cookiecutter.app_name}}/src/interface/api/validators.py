# endregion-------------------------------------------------------------------------
# region API VALIDATORS
# ----------------------------------------------------------------------------------
import datetime

from domain.common.value_object import ValueObjectBase

from lib.dt import convert_datetime_to_ms


def validate_int_value_object(
    value_object: ValueObjectBase[int] | int,
) -> int:
    if isinstance(value_object, ValueObjectBase):
        return value_object.as_raw()

    return value_object


def validate_str_value_object(
    value_object: ValueObjectBase[str] | str,
) -> str:
    if isinstance(value_object, ValueObjectBase):
        return value_object.as_raw()

    return value_object


def validate_float_value_object(
    value_object: ValueObjectBase[float] | float,
) -> float:
    if isinstance(value_object, ValueObjectBase):
        return value_object.as_raw()

    return value_object


def validate_datetime(dt: datetime.datetime | int) -> int:
    if isinstance(dt, int):
        return dt

    if isinstance(dt, datetime.datetime):
        return convert_datetime_to_ms(dt)


# endregion-------------------------------------------------------------------------
