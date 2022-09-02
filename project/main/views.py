from flask import Blueprint, render_template
from project.utils import get_post_all

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    post = get_post_all()
    return render_template("index.html", post=post)
