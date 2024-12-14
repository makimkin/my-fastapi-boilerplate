# endregion-------------------------------------------------------------------------
# region BASE API
# ----------------------------------------------------------------------------------
from application.api.actions import Actions

PREFIX = ""


class BASE_ACTIONS(Actions):
    HEALTHCHECK = "/check/health"


# endregion-------------------------------------------------------------------------
