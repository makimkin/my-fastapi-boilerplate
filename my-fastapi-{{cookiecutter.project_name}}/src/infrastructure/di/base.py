# endregion-------------------------------------------------------------------------
# region BASE DI PROVIDER
# ----------------------------------------------------------------------------------
from dishka import provide, Provider, Scope

from settings.config import Config


class DIProviderBase(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return Config()


# endregion-------------------------------------------------------------------------
