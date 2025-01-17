# endregion-------------------------------------------------------------------------
# region APPLiCATION EXCEPTION HANDLERS
# ----------------------------------------------------------------------------------
import logging

from exceptions import ExceptionBase

from fastapi.exceptions import RequestValidationError
from fastapi import Request, HTTPException, status

logger = logging.getLogger("app")


def base_exception_handler(_: Request, e: ExceptionBase):
    logger.error(e.message, exc_info=e)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
        if e.status_code is None
        else e.status_code,
        detail={
            "error": e.message,
            "name": e.__class__.__name__,
        },
    )


def response_validation_exception_handler(_: Request, e: RequestValidationError):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={
            "error": e.errors(),
            "name": e.__class__.__name__,
        },
    )


# endregion-------------------------------------------------------------------------
