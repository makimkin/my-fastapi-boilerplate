# endregion-------------------------------------------------------------------------
# region REDIS CACHE CONTAINER
# ----------------------------------------------------------------------------------
from dishka import provide, Scope

from redis.asyncio import Redis

from settings.config import Config


class RedisCacheContainer:
    @provide(scope=Scope.APP)
    def get_redis(self, config: Config) -> Redis:
        return Redis.from_url(config.REDIS_URI)


# endregion-------------------------------------------------------------------------
