from sanic import response, Request
import models
from controller import response_wrapper


# POST
async def user_login(req: Request):
    device_uuid = req.args.get("device_uuid")
    if device_uuid is None:
        return response_wrapper.response_msg(response, -1, "device_uuid is None", {})

    firmware = await models.firmware.firmware.all()
    ret = []
    for i in range(len(firmware)):
        ret.append(firmware[i].json())
    for i in ret:
        if str(i["device_uuid"]) != str(device_uuid):
            ret.remove(i)
    _type = req.args.get("type")
    if _type is not None:
        for i in ret:
            if i["type"] != _type:
                ret.remove(i)
    ret = ret[:50] if len(ret) > 50 else ret
    return response.json({"status": 0, "msg": "ok", "data": ret})


# POST
async def user_register(req: Request):
    try:
        _id = req.json.get("id")
        await models.firmware.firmware.filter(id=_id).delete()
        return response.json({"status": 0, "msg": "ok", "data": {}})
    except Exception as e:
        return response_wrapper.response_msg(response, -1, str(e), {})


# POST
async def user_logout(req: Request):
    try:
        _id = req.json.get("id")
        await models.firmware.firmware.filter(id=_id).delete()
        return response.json({"status": 0, "msg": "ok", "data": {}})
    except Exception as e:
        return response_wrapper.response_msg(response, -1, str(e), {})


# GET
async def user_valid_online(req: Request):
    try:
        _id = req.json.get("id")
        await models.firmware.firmware.filter(id=_id).delete()
        return response.json({"status": 0, "msg": "ok", "data": {}})
    except Exception as e:
        return response_wrapper.response_msg(response, -1, str(e), {})
