from flask import Blueprint, jsonify
from project.utils import get_post_all, get_post_by_pk

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/api/posts")
def get_posts_json():
    return jsonify(get_post_all())


@api_blueprint.route("/api/posts/<post_id>")
def get_post__json(post_id):
    return jsonify(get_post_by_pk(post_id))
