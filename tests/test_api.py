import json
import pytest
from app import app

CHECK_KEYS = [
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
]


class TestApi:
    def test_api_posts(self):
        response = app.test_client().get("/api/posts")
        failures = []
        assert response.json
        for post in response.json:
            for check in CHECK_KEYS:
                if post.get(check) == None:
                    failures.append(post)

        assert isinstance(response.json, list)            
        assert [] == failures

    def test_api_post_by_id(self):
        response = app.test_client().get("/api/posts/1")
        failures = []
        for check in CHECK_KEYS:
            if response.json.get(check) == None:
                failures.append(check)

        assert isinstance(response.json, dict)
        assert failures == []
