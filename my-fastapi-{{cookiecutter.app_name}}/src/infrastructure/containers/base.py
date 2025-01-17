# endregion-------------------------------------------------------------------------
# region CONTAINER BASE
# ----------------------------------------------------------------------------------
from settings.config import Config

from dishka import Scope, Provider, provide

from ..authenticator.base import AuthenticatorBase
from ..authenticator.argon import ArgonAuthenticator


class ContainerBase(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return Config()

    def get_authenticator(self, config: Config) -> AuthenticatorBase:
        return ArgonAuthenticator(
            access_token_secret_key=config.AUTH_ACCESS_TOKEN_SECRET_KEY,
            refresh_token_secret_key=config.AUTH_REFRESH_TOKEN_SECRET_KEY,
            access_token_expiration_seconds=config.AUTH_ACCESS_TOKEN_EXPIRATION_SECONDS,
            refresh_token_expiration_seconds=config.AUTH_REFRESH_TOKEN_EXPIRATION_SECONDS,
        )


# endregion-------------------------------------------------------------------------
