"""Shared database and migration extensions."""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class CRUDMixin():
  """Provide small save and delete helpers for SQLAlchemy models."""
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    return

  def save(self):
    db.session.add(self)
    db.session.commit()
    return self

    
