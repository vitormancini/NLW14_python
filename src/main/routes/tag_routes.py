from flask import Blueprint

tags_routes_bp = Blueprint('tags_roues', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tags():
    pass