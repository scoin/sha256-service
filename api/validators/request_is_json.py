from flask import request, abort
import json


def request_is_json(f):
    def closure(*args, **kwargs):
        if request.headers.get("CONTENT-TYPE") != "application/json":
            abort(400, "Must set CONTENT-TYPE header to application/json")
        try:
            json.loads(request.data)
        except Exception, e:
            abort(400, "Invalid JSON")

        return f(*args, **kwargs)

    return closure
