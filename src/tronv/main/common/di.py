from collections.abc import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from tronpy.async_tron import AsyncTron

from tronv.application.view_address import ViewAddress
from tronv.application.view_address_view_logs import ViewAddressViewLogs
from tronv.driven.tronpy.addresses import Addresses
from tronv.driven.typenv.envs import Envs


class ApplicationProvider(Provider):
    provide_runtime_envs = provide(source=Envs.load, scope=Scope.APP)

    @provide(scope=Scope.APP)
    async def provide_engine(
        self, envs: Envs
    ) -> AsyncEngine:
        return create_async_engine(envs.postgres_url, echo=True)

    @provide(scope=Scope.REQUEST)
    async def provide_session(
        self, engine: AsyncEngine
    ) -> AsyncIterator[AsyncSession]:
        session = AsyncSession(
            engine, autoflush=False, autobegin=True, expire_on_commit=False
        )
        async with session:
            yield session

    @provide(scope=Scope.APP)
    async def provide_tron(self) -> AsyncIterator[AsyncTron]:
        async with AsyncTron() as tron:
            yield tron

    provide_addresses = provide(Addresses, scope=Scope.APP)

    provide_view_address = provide(ViewAddress, scope=Scope.REQUEST)

    @provide(scope=Scope.REQUEST)
    async def provide_view_address_view_logs(
        self, session: AsyncSession, envs: Envs
    ) -> ViewAddressViewLogs:
        return ViewAddressViewLogs(session=session, page_size=envs.page_size)
