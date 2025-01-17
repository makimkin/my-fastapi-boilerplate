# endregion-------------------------------------------------------------------------
# region BASE AUTHENTICATOR
# ----------------------------------------------------------------------------------
import datetime
import uuid

from abc import ABC, abstractmethod
from dataclasses import dataclass

from infrastructure.common.base import InfrastructureBase


@dataclass
class AuthenticatorBase(InfrastructureBase, ABC):
    access_token_secret_key: str
    refresh_token_secret_key: str

    access_token_expiration_seconds: int
    refresh_token_expiration_seconds: int

    @abstractmethod
    def generate_access_token(
        self,
        sub: str,
    ) -> tuple[str, datetime.datetime]: ...

    @abstractmethod
    def verify_access_token(self, token: str) -> str: ...

    @abstractmethod
    def generate_refresh_token(
        self,
        sub: str,
    ) -> tuple[str, datetime.datetime]: ...

    @abstractmethod
    def verify_refresh_token(self, token: str) -> str: ...

    @abstractmethod
    def verify_password(self, password: str, hashed_password: str) -> bool: ...

    @abstractmethod
    def hash_password(self, password: str) -> str: ...

    async def check_health(self) -> bool:
        sub = str(uuid.uuid4())

        access_token, *_ = self.generate_access_token(sub)
        refresh_token, *_ = self.generate_refresh_token(sub)

        return (
            self.verify_access_token(access_token) == sub
            and self.verify_refresh_token(refresh_token) == sub
        )


# endregion-------------------------------------------------------------------------
