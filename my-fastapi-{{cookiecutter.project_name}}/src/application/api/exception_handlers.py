# endregion-------------------------------------------------------------------------
# region APPLiCATION EXCEPTION HANDLERS
# ----------------------------------------------------------------------------------
import logging

from application.exceptions import BaseApplicationException

from fastapi import Request, HTTPException, status

logger = logging.getLogger("app")


def base_exception_handler(_: Request, e: BaseApplicationException):
    logger.exception(e)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={
            "error": e.message,
            "name": e.__class__.__name__,
        },
    )


# endregion-------------------------------------------------------------------------
