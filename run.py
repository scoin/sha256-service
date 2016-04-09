from flask import Flask, jsonify, make_response
from api.controllers.hashes import hashes
from api.models.hash import Hash


def create_app():
    app = Flask(__name__)

    app.register_blueprint(hashes, url_prefix="/hash")
    app = error_routes(app)

    app.db = Hash()

    return app


def error_routes(app):

    @app.errorhandler(500)
    def server_error(e):
        print(e)
        return make_response(jsonify({
            "error": "Whoops, Server Error",
            "message": e.description,
            "status": 500
        }), 500)

    @app.errorhandler(404)
    def not_found_error(e):
        return make_response(jsonify({
            "error": "The Request Resource Was Not Found",
            "message": e.description,
            "status": 404
        }), 404)

    @app.errorhandler(400)
    def bad_request_error(e):
        return make_response(jsonify({
            "error": "Bad Request - Your Request Could Not Be Fulfilled",
            "message": e.description,
            "status": 400
        }), 400)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
