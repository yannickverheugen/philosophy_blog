from unittest.mock import patch

from app.app import create_app
from app.users import routes


def test_post_register_uses_username_from_form():
    app = create_app()
    created_users = []

    class DummyQuery:
        def filter_by(self, **kwargs):
            return self

        def first(self):
            return None

    class DummyUser:
        query = DummyQuery()

        def __init__(self, **kwargs):
            created_users.append(kwargs)

        def save(self):
            return self

    with patch("app.users.routes.User", DummyUser):
        with app.test_request_context(
            "/register",
            method="POST",
            data={
                "email": "alice@example.com",
                "username": "alice",
                "password": "secret123",
                "password_confirmation": "secret123",
            },
        ):
            response = routes.post_register()

    assert response.status_code == 302
    assert response.location.endswith("/articles")
    assert created_users[0]["username"] == "alice"
