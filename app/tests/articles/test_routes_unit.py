from unittest.mock import patch

from app.app import create_app
from app.articles import routes


def test_article_redirects_when_slug_missing():
    app = create_app()

    class DummyQuery:
        def filter_by(self, **kwargs):
            assert kwargs == {"slug": "missing-slug"}
            return self

        def first(self):
            return None

    class DummyArticle:
        query = DummyQuery()

    with patch("app.articles.routes.Article", DummyArticle):
        with app.test_request_context("/articles/missing-slug"):
            response = routes.article("missing-slug")

    assert response.status_code == 302
    assert response.location.endswith("/articles")


def test_article_renders_template_when_slug_exists():
    app = create_app()
    fake_article = object()

    class DummyQuery:
        def filter_by(self, **kwargs):
            assert kwargs == {"slug": "existing-slug"}
            return self

        def first(self):
            return fake_article

    class DummyArticle:
        query = DummyQuery()

    with patch("app.articles.routes.Article", DummyArticle):
        with patch("app.articles.routes.render_template", return_value="rendered") as render_mock:
            with app.test_request_context("/articles/existing-slug"):
                response = routes.article("existing-slug")

    assert response == "rendered"
    render_mock.assert_called_once_with("article.html", article=fake_article)


def test_list_articles_uses_requested_page_and_configured_page_size():
    app = create_app()
    fake_pagination = object()

    class DummyQuery:
        def __init__(self):
            self.called_with = None

        def paginate(self, **kwargs):
            self.called_with = kwargs
            return fake_pagination

    dummy_query = DummyQuery()

    class DummyArticle:
        query = dummy_query

    with patch("app.articles.routes.Article", DummyArticle):
        with patch("app.articles.routes.render_template", return_value="rendered") as render_mock:
            with app.test_request_context("/articles?page=3"):
                response = routes.list_articles()

    assert response == "rendered"
    assert dummy_query.called_with == {
        "page": 3,
        "per_page": app.config["ARTICLES_PER_PAGE"],
    }
    render_mock.assert_called_once_with("articles/articles.html", articles=fake_pagination)