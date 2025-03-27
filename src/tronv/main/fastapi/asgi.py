from tronv.driver.fastapi.app import app_from
from tronv.main.common.asgi import LazyASGIApp
from tronv.main.fastapi.di import container


app = LazyASGIApp(app_factory=lambda: app_from(container))
