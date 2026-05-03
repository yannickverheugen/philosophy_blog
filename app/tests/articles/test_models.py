from app.extensions.database import db
from app.articles.models import Article
from app.users.models import User

def test_article_create(client):
    user = User(username='test_author_create', email='test_author_create@example.com', password='test-password')
    db.session.add(user)
    db.session.commit()

    article = Article(
        slug='test-article-create',
        title='Test Article Create',
        content='This is a test article that is created and stored.',
        author_id=user.id,
    )

    article.save()

    created_article = Article.query.filter_by(slug='test-article-create').first()
    assert created_article is not None
    assert created_article.title == 'Test Article Create'

def test_article_update(client):
    # create a user to associate with the article
    user = User(username ='test_author', email ='test_author@example.com', password ='test-password')
    db.session.add(user)
    db.session.commit()

    # updates articles property
    article = Article(slug='test-article', title='Test Article', content='This is a test article.', author_id=user.id)

    db.session.add(article)
    db.session.commit()

    article.title = 'Updated Test Article'
    article.save()

    updated_article = Article.query.filter_by(slug='test-article').first()
    assert updated_article.title == 'Updated Test Article'

def test_article_delete(client):
    # create a user to associate with the article
    # create a user to associate with the article
    user = User(username ='test_author', email ='test_author@example.com', password ='test-password')
    db.session.add(user)
    db.session.commit()

    article = Article(slug='test-article-to-delete', title='Test Article to Delete', content='This article will be deleted.', author_id=user.id)
    db.session.add(article)
    db.session.commit()

    article.delete()

    deleted_article = Article.query.filter_by(slug='test-article-to-delete').first()
    assert deleted_article is None
