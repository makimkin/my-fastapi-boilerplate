# endregion-------------------------------------------------------------------------
# region SQL REPOSITORIES CONTAINER
# ----------------------------------------------------------------------------------
from dishka import provide, Scope

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from settings.config import Config


class SQLRepositoriesContainer:
    @provide(scope=Scope.APP)
    def get_sql_session_maker(
        self,
        config: Config,
    ) -> async_sessionmaker[AsyncSession]:
        engine = create_async_engine(config.SQL_URI, echo=True, future=True)

        return async_sessionmaker(
            expire_on_commit=False,
            class_=AsyncSession,
            autoflush=False,
            bind=engine,
        )


# endregion-------------------------------------------------------------------------
