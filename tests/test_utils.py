import pytest
from project.utils import (
    get_comments_by_post_id,
    get_post_all,
    get_posts_by_pk,
    get_posts_by_user,
    search_for_posts,
)


class UtilsTest:
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
        data = get_post_all()
        failures = []
        for post in data:
            for check in checks:
                if post.get(check) != None:
                    failures.append(post)
        assert failures == [], "Посты повреждены, чего-то явно не хватает"
