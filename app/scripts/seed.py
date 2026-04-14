from app.app import create_app
from app.articles.models import Article
from app.users.models import User
from app.extensions.database import db
from datetime import datetime

def seed_users() -> dict[str, int]:
  users_data = [
    {
      'username': 'socrates',
      'email': 'socrates@example.com',
      'password': 'seed-password',
    },
    {
      'username': 'plato',
      'email': 'plato@example.com',
      'password': 'seed-password',
    },
    {
      'username': 'aristotle',
      'email': 'aristotle@example.com',
      'password': 'seed-password',
    },
  ]

  for user_data in users_data:
    existing_user = User.query.filter_by(email=user_data['email']).first()
    if not existing_user:
      db.session.add(User(**user_data))

  db.session.commit()
  return {user.username: user.id for user in User.query.all()}


def seed_articles(author_ids: dict[str, int]) -> None:
  articles_data = {
    'the-unexamined-life': {
      'title': 'The Unexamined Life',
      'content': 'The unexamined life is not worth living. We must question everything we think we know.',
      'created_at': datetime(2026, 4, 1, 10, 0, 0),
      'author_username': 'socrates',
    },
    'the-allegory-of-the-cave': {
      'title': 'The Allegory of the Cave',
      'content': 'Imagine prisoners chained in a cave, only seeing shadows on the wall. What if one broke free?',
      'created_at': datetime(2026, 4, 3, 14, 30, 0),
      'author_username': 'plato',
    },
    'the-golden-mean': {
      'title': 'The Golden Mean',
      'content': 'Virtue lies in finding the balance between excess and deficiency.',
      'created_at': datetime(2026, 4, 5, 9, 15, 0),
      'author_username': 'aristotle',
    },
    'beyond-good-and-evil': {
      'title': 'Beyond Good and Evil',
      'content': 'Nietzsche challenged conventional morality, arguing that good and evil are human constructs.',
      'created_at': datetime(2026, 4, 7, 16, 45, 0),
      'author_username': 'socrates',
    },
    'existence-precedes-essence': {
      'title': 'Existence Precedes Essence',
      'content': 'Sartre argued that humans are not born with a predetermined purpose. We must create our own meaning.',
      'created_at': datetime(2026, 4, 9, 11, 0, 0),
      'author_username': 'plato',
    },
  }

  for slug, article in articles_data.items():
    if Article.query.filter_by(slug=slug).first():
      continue

    author_id = author_ids.get(article['author_username'])
    if not author_id:
      continue

    new_article = Article(
      slug=slug,
      title=article['title'],
      content=article['content'],
      created_at=article['created_at'],
      author_id=author_id,
    )
    db.session.add(new_article)

  db.session.commit()


def main() -> None:
  app = create_app()
  with app.app_context():
    author_ids = seed_users()
    seed_articles(author_ids)


if __name__ == '__main__':
  main()