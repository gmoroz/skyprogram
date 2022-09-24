import json
from project.functions import load_data
from project.post_helpers import get_post_by_pk
import copy


def add_bookmark(post_id: str) -> None:
    """Данная функция добавляет пост
    по переданному id в закладки"""
    bookmarks_posts = load_data("project/data/bookmarks.json")
    post = get_post_by_pk(post_id)
    all_posts = load_data("project/data/posts.json")
    if post not in bookmarks_posts:
        index = next(i for i, post_ in enumerate(all_posts) if post_ == post)
        all_posts[index]["is_bookmark"] = True
        post["is_bookmark"] = True
        bookmarks_posts.append(post)

    json_write(bookmarks_posts, "project/data/bookmarks.json")
    json_write(all_posts, "project/data/posts.json")


def remove_bookmark(post_id: str):
    """Данная функция удаляет пост
    по переданному id из закладок"""
    bookmarks_posts = load_data("project/data/bookmarks.json")
    post = get_post_by_pk(post_id)
    all_posts = load_data("project/data/posts.json")
    if post in bookmarks_posts:
        index = next(i for i, post_ in enumerate(all_posts) if post_ == post)
        all_posts[index]["is_bookmark"] = False
        bookmarks_posts.remove(post)

    json_write(bookmarks_posts, "project/data/bookmarks.json")
    json_write(all_posts, "project/data/posts.json")


def json_write(data: list[dict], filename) -> None:
    """Данная функция сохраняет переданную информацию
    в json файл"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def get_bookmarks() -> list[dict]:
    return load_data("project/data/bookmarks.json")
