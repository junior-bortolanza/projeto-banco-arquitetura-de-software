from flask import Blueprint, jsonify

pessoa_fisica_route_bp = Blueprint('pessoa_fisica_routes', __name__)

@pessoa_fisica_route_bp.route("/pessoa_fisica", methods=['GET'])
def list_pessoa_fisica():
    return jsonify({"message": "Olá mundo"}), 200
