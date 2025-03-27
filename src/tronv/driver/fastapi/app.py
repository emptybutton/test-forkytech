from collections.abc import AsyncIterator, Iterable
from contextlib import asynccontextmanager

from dishka import AsyncContainer
from dishka.integrations.fastapi import setup_dishka
from fastapi import APIRouter, FastAPI

from tronv.driver.fastapi.tags import tags_metadata


type FastAPIAppRouters = Iterable[APIRouter]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    await app.state.dishka_container.close()


async def app_from(container: AsyncContainer) -> FastAPI:
    version = "0.1.0"
    author_url = "https://github.com/emptybutton"
    repo_name = "tronv"
    repo_url = f"{author_url}/{repo_name}"

    app = FastAPI(
        title=repo_name,
        version=version,
        description="Тестовое задание для компании Форкитех.",
        openapi_tags=tags_metadata,
        contact={"name": "Alexander Smolin", "url": author_url},
        license_info={
            "name": "Apache 2.0",
            "url": f"{repo_url}/blob/main/LICENSE",
        },
        lifespan=lifespan,
        root_path=f"/api/{version}",
    )

    routers = await container.get(FastAPIAppRouters)

    for router in routers:
        app.include_router(router)

    setup_dishka(container=container, app=app)

    return app
