# endregion-------------------------------------------------------------------------
# region BASE DI PROVIDER
# ----------------------------------------------------------------------------------
from settings.config import Config

from dishka import Scope, Provider, provide

class DIProviderBase(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return Config()


# endregion-------------------------------------------------------------------------
