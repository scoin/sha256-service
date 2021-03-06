from flask import request, Blueprint, jsonify, make_response, abort, current_app
from api.validators.request_is_json import request_is_json
from api.validators.param_is_sha256 import param_is_sha256
from api.models.hash import Hash


hashes = Blueprint("hash", __name__)


@hashes.route("/", methods=["POST"], strict_slashes=False)
@request_is_json
def post_hash():
    hash_output = current_app.db.save(request.get_json())
    return make_response(jsonify({"hash": hash_output}), 201)


@hashes.route("/<hashstring>", methods=["GET"], strict_slashes=False)
@param_is_sha256
def get_hash(hashstring):
    json_data = current_app.db.get(hashstring)
    if(json_data is None):
        abort(404, "{key} not found".format(key=hashstring))
    return jsonify(json_data)
