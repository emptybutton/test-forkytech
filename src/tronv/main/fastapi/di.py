from dishka import Provider, Scope, make_async_container, provide

from tronv.driver.fastapi.app import FastAPIAppRouters
from tronv.driver.fastapi.routers import all_routers
from tronv.main.common.di import ApplicationProvider


class FastApiProvider(Provider):
    scope = Scope.APP

    @provide
    def provide_routers(self) -> FastAPIAppRouters:
        return all_routers


container = make_async_container(
    FastApiProvider(),
    ApplicationProvider(),
)
