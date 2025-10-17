# from sanic_compress import Compress
from sanic import Sanic, response

app = Sanic("App")
# Compress(app)

# register cors
from cors.cors import register_cors

app = register_cors(app)
# end

from config.app_config import APPX_PATH

# app.static(uri="/", name="webx", file_or_directory=WEBX_PATH)


async def fetch_file(prefix, uri):
    return await response.file(prefix + uri)


from router.appx import register_router_appx

app = register_router_appx(app)


from controller.file import file_fetch, file_remove, file_upload


app.add_route(
    handler=file_upload,
    uri="/api/v1/file/upload",
    methods=["POST"],
)

app.add_route(
    handler=file_fetch,
    uri="/api/v1/file/fetch",
    methods=["GET"],
)

app.add_route(
    handler=file_remove,
    uri="/api/v1/file/remove",
    methods=["GET"],
)


from tortoise.contrib.sanic import register_tortoise
from sanic import Sanic
from config.database import get_db_url


def register_databases(_app: Sanic):
    register_tortoise(
        _app,
        db_url=get_db_url(),
        modules={"models": ["models.user"]},
        generate_schemas=True,
    )
    return _app


app = register_databases(app)

# app.config.CORS_ORIGINS = "http://localhost:5173"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5174)
