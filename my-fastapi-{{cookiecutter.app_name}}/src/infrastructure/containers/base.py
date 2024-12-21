# endregion-------------------------------------------------------------------------
# region CONTAINER BASE
# ----------------------------------------------------------------------------------
from settings.config import Config

from dishka import Scope, Provider, provide


class ContainerBase(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        return Config()


# endregion-------------------------------------------------------------------------
