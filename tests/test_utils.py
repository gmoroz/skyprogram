import pytest
from project.utils import (
    get_comments_by_post_id,
    get_post_all,
    get_post_by_pk,
    get_posts_by_user,
    search_for_posts,
)


class TestUtils:
    def test_get_post_all(self):
        checks = [
            "poster_name",
            "poster_avatar",
            "pic",
            "content",
            "views_count",
            "likes_count",
            "pk",
        ]
        posts = get_post_all()
        failures = []
        for post in posts:
            for check in checks:
                if post.get(check) == None:
                    failures.append(post)
        assert failures == [], "Посты повреждены, чего-то явно не хватает"

    def test_get_post_by_user(self):
        user_posts = get_posts_by_user("larry")
        assert len(user_posts) == 2
        assert get_posts_by_user("asdf") == []

    def test_get_comments_by_post_id(self):
        try:
            get_comments_by_post_id(342)
        except ValueError:
            assert True
        comments = get_comments_by_post_id(7)
        check = {
            "post_id": 7,
            "commenter_name": "hanna",
            "comment": "Очень необычная фоторафия! Где это?",
            "pk": 20,
        }
        assert check in comments

    def test_search_for_posts(self):
        query = "РАНЬШЕ"
        posts = search_for_posts(query)
        failures = []
        for post in posts:
            if query.lower() not in post["content"].lower():
                failures.append(post)
        assert failures == []

    def test_get_post_by_pk(self):
        assert {} == get_post_by_pk(328)
        post = get_post_by_pk(8)
        assert post.get("content") != None
        assert post.get("likes_count") == 45
