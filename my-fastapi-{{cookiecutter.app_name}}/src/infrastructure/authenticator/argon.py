# endregion-------------------------------------------------------------------------
# region HS256 AUTH
# ----------------------------------------------------------------------------------
import datetime
import jwt

from argon2 import PasswordHasher
from dataclasses import dataclass

from .exceptions import (
    AuthenticatorExpiredRefreshTokenException,
    AuthenticatorInvalidRefreshTokenException,
    AuthenticatorExpiredAccessTokenException,
    AuthenticatorInvalidAccessTokenException,
)

from .base import AuthenticatorBase


@dataclass
class ArgonAuthenticator(AuthenticatorBase):
    def generate_access_token(
        self,
        sub: str,
    ) -> tuple[str, datetime.datetime]:
        return self._generate_token(
            sub,
            secret_key=self.access_token_secret_key,
            expiration_seconds=self.access_token_expiration_seconds,
        )

    def verify_access_token(self, token: str) -> str:
        try:
            return self._verify_token_and_get_sub(
                token,
                secret_key=self.access_token_secret_key,
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticatorExpiredAccessTokenException() from None
        except jwt.InvalidTokenError:
            raise AuthenticatorInvalidAccessTokenException() from None

    def generate_refresh_token(
        self,
        sub: str,
    ) -> tuple[str, datetime.datetime]:
        return self._generate_token(
            sub,
            secret_key=self.refresh_token_secret_key,
            expiration_seconds=self.refresh_token_expiration_seconds,
        )

    def verify_refresh_token(self, token: str) -> str:
        try:
            return self._verify_token_and_get_sub(
                token,
                secret_key=self.refresh_token_secret_key,
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticatorExpiredRefreshTokenException() from None
        except jwt.InvalidTokenError:
            raise AuthenticatorInvalidRefreshTokenException() from None

    def verify_password(self, password: str, hashed_password: str) -> bool:
        try:
            hasher = PasswordHasher()
            return hasher.verify(hashed_password, password)
        except Exception:
            return False

    def hash_password(self, password: str) -> str:
        hasher = PasswordHasher()
        return hasher.hash(password)

    def _generate_token(
        self,
        sub: str,
        *,
        secret_key: str,
        expiration_seconds: int,
    ) -> tuple[str, datetime.datetime]:
        exp = datetime.datetime.now() + datetime.timedelta(seconds=expiration_seconds)

        return jwt.encode(
            {
                "sub": sub,
                "exp": exp,
            },
            secret_key,
            algorithm="HS256",
        ), exp

    def _verify_token_and_get_sub(
        self,
        token: str,
        *,
        secret_key: str,
    ) -> str:
        payload = jwt.decode(
            token,
            secret_key,
            algorithms=["HS256"],
        )

        return payload.get("sub")


# endregion-------------------------------------------------------------------------
