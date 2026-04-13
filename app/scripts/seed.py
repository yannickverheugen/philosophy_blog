from app.app import create_app
from app.articles.models import Article
from app.users.models import User
from app.extensions.database import db
from datetime import datetime

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

articles_data = {
    'the-unexamined-life': {'title': 'The Unexamined Life', 'content': 'The unexamined life is not worth living. We must question everything we think we know.', 'created_at': datetime(2026, 4, 1, 10, 0, 0), 'author_id': 1},
    'the-allegory-of-the-cave': {'title': 'The Allegory of the Cave', 'content': 'Imagine prisoners chained in a cave, only seeing shadows on the wall. What if one broke free?', 'created_at': datetime(2026, 4, 3, 14, 30, 0), 'author_id': 2},
    'the-golden-mean': {'title': 'The Golden Mean', 'content': 'Virtue lies in finding the balance between excess and deficiency.', 'created_at': datetime(2026, 4, 5, 9, 15, 0), 'author_id': 3},
    'beyond-good-and-evil': {'title': 'Beyond Good and Evil', 'content': 'Nietzsche challenged conventional morality, arguing that good and evil are human constructs.', 'created_at': datetime(2026, 4, 7, 16, 45, 0), 'author_id': 1},
    'existence-precedes-essence': {'title': 'Existence Precedes Essence', 'content': 'Sartre argued that humans are not born with a predetermined purpose. We must create our own meaning.', 'created_at': datetime(2026, 4, 9, 11, 0, 0), 'author_id': 2},
}

for slug, article in articles_data.items():
    new_article = Article(slug=slug, title=article['title'], content=article['content'], created_at=article['created_at'], author_id=article['author_id'])
    db.session.add(new_article)

db.session.commit()