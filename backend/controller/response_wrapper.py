import sanic
import json


def response_msg(response: sanic.response, status_code: int, msg: str, payload: json):
    return response.json({"status": status_code, "msg": msg, "data": payload})
