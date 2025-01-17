# endregion-------------------------------------------------------------------------
# region MIDDLEWARES
# ----------------------------------------------------------------------------------
import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


logger = logging.getLogger("app")


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        logger.info(
            f"{request.method} {request.url} completed in {process_time:.2f}s"
        )

        response.headers["X-Process-Time"] = str(process_time)

        return response


# endregion-------------------------------------------------------------------------
