from app.extensions.database import db
from app.articles.models import Article
from app.users.models import User

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
