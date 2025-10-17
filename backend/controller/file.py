from sanic import Request, response
from controller import response_wrapper
import models


# POST
async def file_upload(req: Request):
    try:
        import aiofiles
        import os
        from config import app_config

        if not os.path.exists(app_config.FILE_PATH):
            os.makedirs(app_config.FILE_PATH)
        from utils import tools

        _md5_sum = tools.calculate_md5_raw(req.files["file"][0].body)
        filepath = app_config.FILE_PATH + "/" + _md5_sum

        if os.path.exists(filepath):
            return response.json(
                {"status": 0, "msg": "ok", "data": {"md5sum": _md5_sum}}
            )

        async with aiofiles.open(filepath, "wb") as f:
            await f.write(req.files["file"][0].body)

        await f.close()
        return response.json({"status": 0, "msg": "ok", "data": {"md5sum": _md5_sum}})

    except Exception as e:
        return response_wrapper.response_msg(response, -1, str(e), {})


# GET
async def file_fetch(req: Request):
    try:
        import os
        from config import app_config

        _object = req.args.get("object")
        # print(_object)

        file_path = os.path.join(app_config.FILE_PATH, _object)
        # print(file_path)
        if not os.path.exists(file_path):
            return response_wrapper.response_msg(response, -1, "File not found", {})

        with open(file_path, "rb") as f:
            file_bytes = f.read()

        content_type = "application/octet-stream"
        from sanic.response import raw

        return raw(file_bytes, headers={"Content-Type": content_type})

    except Exception as e:
        return response_wrapper.response_msg(response, -1, str(e), {})


# GET
async def file_remove(req: Request):
    try:
        import os
        from config import app_config

        _object = req.args.get("object")
        # print(_object)

        firmware = await models.firmware.firmware.filter(hash_sum=_object)
        if len(firmware) > 0:
            return response_wrapper.response_msg(
                response, -1, "table firmware limit", {}
            )

        file_path = os.path.join(app_config.FILE_PATH, _object)
        # print(file_path)
        if not os.path.exists(file_path):
            return response_wrapper.response_msg(response, -1, "File not found", {})

        os.remove(file_path)
        return response_wrapper.response_msg(response, 0, "ok", {})

    except Exception as e:
        return response_wrapper.response_msg(response, -1, str(e), {})
