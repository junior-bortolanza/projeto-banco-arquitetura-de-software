from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pessoa_juridica_create_composer import pessoa_juridica_create_composer
from src.main.composer.pessoa_juridica_lister_composer import pessoa_juridica_lister_composer
from src.main.composer.pessoa_juridica_realizar_saque_composer import pessoa_juridica_realizar_saque_composer

from src.errors.error_handler import handle_errors

pessoa_juridica_routes_bp = Blueprint("pessoa_juridica_routes", __name__)

@pessoa_juridica_routes_bp.route('/pessoajuridica', methods=['POST'])
def create_pessoa_juridica():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_juridica_create_composer()

        http_response = view.handle(http_request)
        return jsonify(http_request.body), http_response.status_code
    except Exception as exception:
        http_response  = handle_errors(exception)
        return jsonify(http_request.body), http_response.status_code

@pessoa_juridica_routes_bp.route('/pessoajuridica', methods=['GET'])
def lister_pessoa_juridica():
    try:
        http_request = HttpRequest()
        view = pessoa_juridica_lister_composer()

        http_response = view.handle(http_request)
        return jsonify(http_request.body), http_response.status_code
    except Exception as exception:
        http_response  = handle_errors(exception)
        return jsonify(http_request.body), http_response.status_code

@pessoa_juridica_routes_bp.route('/pessoajuridica', methods=['PATCH'])
def saque_pessoa_juridica():
    try:
        http_request = HttpRequest(body=request.json)
        view = pessoa_juridica_realizar_saque_composer()

        http_response = view.handle(http_request)
        return jsonify(http_request.body), http_response.status_code
    except Exception as exception:
        http_response  = handle_errors(exception)
        return jsonify(http_request.body), http_response.status_code
