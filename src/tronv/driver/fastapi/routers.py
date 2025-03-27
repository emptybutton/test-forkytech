from collections.abc import Iterator

from fastapi import APIRouter

from tronv.driver.fastapi.routes.healthcheck import (
    healthcheck_router,
)
from tronv.driver.fastapi.routes.view_address import (
    view_address_router,
)
from tronv.driver.fastapi.routes.view_address_view_logs import (
    view_address_view_logs_router,
)


all_routers = (
    view_address_router,
    view_address_view_logs_router,
    healthcheck_router,
)


class UnknownRouterError(Exception): ...


def ordered(*routers: APIRouter) -> Iterator[APIRouter]:
    for router in all_routers:
        if router not in routers:
            raise UnknownRouterError

        yield router
