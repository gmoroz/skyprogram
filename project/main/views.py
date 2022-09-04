import logging
from flask import Blueprint, render_template, request
from project.utils import (
    get_comments_by_post_id,
    get_post_all,
    get_post_by_pk,
    get_posts_by_user,
    get_suffix,
    search_by_tag,
    search_for_posts,
)

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    posts = get_post_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/posts/<post_id>")
def show_post_page(post_id):
    try:
        post = get_post_by_pk(post_id)
        comments = get_comments_by_post_id(post_id)
        return render_template(
            "post.html",
            post=post,
            comments=comments,
            comments_count=get_suffix(len(comments)),
        )
    except ValueError:
        return "Такого поста нет"


@main_blueprint.route("/tag/<tag_name>")
def tag_page(tag_name):
    posts = search_by_tag("#" + tag_name)
    if posts:
        return render_template("search_by_tag.html", posts=posts, posts_count=len(posts))
    return "По вашему запросу ничего не найдено"


@main_blueprint.route("/search/")
def search_page():
    s = request.args.get("s")
    posts = search_for_posts(s)
    return render_template("search.html", posts=posts, posts_count=len(posts))


@main_blueprint.route("/users/<username>")
def user_page(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts)
