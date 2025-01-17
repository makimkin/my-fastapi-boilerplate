# endregion-------------------------------------------------------------------------
# region AUTHENTICATOR EXCEPTIONS
# ----------------------------------------------------------------------------------
from dataclasses import dataclass

from fastapi import status

from ..exceptions import InfrastructureExceptionBase


@dataclass(frozen=False)
class AuthenticatorExceptionBase(InfrastructureExceptionBase):
    @property
    def message(self) -> str:
        return "Authenticator Exception"

    @property
    def status_code(self) -> int:
        return status.HTTP_401_UNAUTHORIZED


@dataclass(frozen=False)
class AuthenticatorExpiredAccessTokenException(AuthenticatorExceptionBase):
    @property
    def message(self) -> str:
        return "Access token expired"


@dataclass(frozen=False)
class AuthenticatorInvalidAccessTokenException(AuthenticatorExceptionBase):
    @property
    def message(self) -> str:
        return "Invalid access token"


@dataclass(frozen=False)
class AuthenticatorExpiredRefreshTokenException(AuthenticatorExceptionBase):
    @property
    def message(self) -> str:
        return "Refresh token expired"


@dataclass(frozen=False)
class AuthenticatorInvalidRefreshTokenException(AuthenticatorExceptionBase):
    @property
    def message(self) -> str:
        return "Invalid refresh token"


# endregion-------------------------------------------------------------------------
