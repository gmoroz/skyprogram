from flask import Blueprint, redirect, render_template
from project.bookmarks.utils import add_bookmark, get_bookmarks, remove_bookmark

bookmarks_blueprint = Blueprint(
    "bookmarks_blueprint", __name__, template_folder="templates"
)


@bookmarks_blueprint.route("/bookmarks/add/<post_id>")
def page_bookmark_add(post_id):
    add_bookmark(post_id)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<post_id>")
def page_bookmark_remove(post_id):
    remove_bookmark(post_id)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/")
def page_bookmarks():
    posts = get_bookmarks()
    return render_template("bookmarks.html", posts=posts)
