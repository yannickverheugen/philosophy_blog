from app.app import create_app
from app.simple_pages.routes import contact_post


def test_contact_post_formats_response_text():
    app = create_app()

    with app.test_request_context(
        "/contact",
        method="POST",
        data={
            "user_name": "Ada",
            "user_email": "ada@example.com",
            "user_message": "I enjoy your blog.",
        },
    ):
        response_text = contact_post()

    assert response_text == (
        'Thank you Ada for your message: "I enjoy your blog.". '
        "We will contact you at ada@example.com."
    )