# endregion-------------------------------------------------------------------------
# region APPLiCATION EXCEPTION HANDLERS
# ----------------------------------------------------------------------------------
import logging

from domain.common.exceptions import ExceptionBase

from fastapi import Request, HTTPException, status

logger = logging.getLogger("app")


def base_exception_handler(_: Request, e: ExceptionBase):
    logger.error(e.message, exc_info=e)
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={
            "error": e.message,
            "name": e.__class__.__name__,
        },
    )


# endregion-------------------------------------------------------------------------
