
from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pessoa_fisica_create_composer import pessoa_fisica_create_composer
from src.main.composer.pessoa_fisica_lister_composer import pessoa_fisica_lister_composer
from src.main.composer.pessoa_fisica_realizar_saque_composer import pessoa_fisica_realizar_saque_composer

from src.errors.error_handler import handle_errors

pessoa_fisica_route_bp = Blueprint('pessoa_fisica_routes', __name__)

@pessoa_fisica_route_bp.route("/pessoafisica", methods=['POST'])
def create_pessoa_fisica():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_fisica_create_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/pessoafisica", methods=['GET'])
def lister_pessoa_fisica():
    try:
        http_request = HttpRequest()
        view = pessoa_fisica_lister_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pessoa_fisica_route_bp.route("/saque", methods=['PATCH'])
def saque_pessoa_fisica():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_fisica_realizar_saque_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
