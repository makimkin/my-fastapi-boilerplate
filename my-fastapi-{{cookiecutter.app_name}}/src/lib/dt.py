# endregion-------------------------------------------------------------------------
# region DATETIME
# ----------------------------------------------------------------------------------
import datetime


# endregion-------------------------------------------------------------------------
# region DATETIME TO MS
# ----------------------------------------------------------------------------------
def convert_datetime_to_ms(dt: datetime.datetime) -> int:
    return int(dt.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)


# endregion-------------------------------------------------------------------------
# region MS TO DATETIME
# ----------------------------------------------------------------------------------
def convert_ms_to_datetime(ts: int) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(ts / 1000, tz=datetime.timezone.utc)


# endregion-------------------------------------------------------------------------
