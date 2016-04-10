from flask import request, abort


def param_is_sha256(f):
    def sha256_check(*args, **kwargs):
        hashstring = kwargs.get('hashstring')

        if hashstring is None:
            abort(400, "SHA256 hash required")

        hashbytes = bytes(hashstring)

        if len(hashbytes) < 64:
            abort(400, "Provided Parameter is not SHA256")

        return f(*args, **kwargs)

    return sha256_check
