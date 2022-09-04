import json
from project.functions import load_data
from project.utils import get_post_by_pk
import copy


def add_bookmark(post_id: str) -> None:
    """Данная функция добавляет пост
    по переданному id в закладки"""
    bookmarks_posts = load_data("project/data/bookmarks.json")
    post = get_post_by_pk(post_id)
    if post not in bookmarks_posts:
        bookmarks_posts.append(post)
    json_write(bookmarks_posts)


def remove_bookmark(post_id: str):
    """Данная функция удаляет пост
    по переданному id из закладок"""
    bookmarks_posts = load_data("project/data/bookmarks.json")
    posts = copy.deepcopy(bookmarks_posts)
    post = get_post_by_pk(post_id)
    for bookmark_post in bookmarks_posts:
        if bookmark_post["pk"] == post["pk"]:
            posts.remove(post)
            break
    json_write(posts)


def json_write(data: list[dict]) -> None:
    """Данная функция сохраняет закладки
    в json файл"""
    with open("project/data/bookmarks.json", "w") as file:
        json.dump(data, file)


def get_bookmarks() -> list[dict]:
    return load_data("project/data/bookmarks.json")
