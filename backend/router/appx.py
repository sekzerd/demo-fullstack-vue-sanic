from sanic import Sanic, response, Request
from config.app_config import APPX_PATH


async def appx_entry(request: Request):
    path = request.path
    return await response.file(path + "/index.html")


def register_router_appx(app: Sanic):
    app.add_route(
        name="default entry",
        handler=appx_entry,
        uri="/",
        methods=["GET"],
        strict_slashes=False,
    )

    return app
