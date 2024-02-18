from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import handle_errors

tags_routes_bp = Blueprint('tags_roues', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tags():
    response = None
    try:
        http_request = HttpRequest(body = request.json) # Obtém o corpo da requisição
        tag_creator_view = TagCreatorView()
        response = tag_creator_view.validate_and_create(http_request) # Invoca o serviço de validação e criação de tags
    except Exception as e:
        response = handle_errors(e)

    return jsonify(response.body), response.status_code