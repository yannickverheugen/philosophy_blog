# Philosophy Blog

A Flask-based blog application focused on philosophy content. The app uses:

- Flask for routing and templates
- Flask-SQLAlchemy for ORM/database access
- Flask-Migrate/Alembic for schema migrations
- Gunicorn for production serving

## Features

- Home, About, Topics, and Contact pages
- Articles listing and article detail pages
- Pagination support for article lists
- Seed script for initial users and articles
- Render-ready configuration with Postgres support

## Project Structure

- `run.py`: Flask app entrypoint (and Gunicorn app object)
- `app/app.py`: app factory and extension/blueprint registration
- `app/config.py`: environment-based app config
- `app/articles/`: article models and routes
- `app/users/`: user model
- `app/scripts/seed.py`: idempotent seed script
- `app/templates/`: Jinja templates
- `app/static/`: static assets (CSS/images)
- `migrations/`: Alembic migration files

## Requirements

Use the root `requirements.txt` as the canonical dependency file.

## Local Development

### 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in project root:

```env
SECRET_KEY=change-me
DATABASE_URL=sqlite:///app.db
```

Notes:
- In production, `DATABASE_URL` should point to Postgres.
- The app normalizes `postgres://` to `postgresql://` automatically.

### 4. Run migrations

```bash
python -m flask --app run db upgrade
```

### 5. Seed initial data (optional)

```bash
python -m app.scripts.seed
```

The seed script is idempotent:
- Existing users (matched by email) are skipped
- Existing articles (matched by slug) are skipped

### 6. Start the app

```bash
python run.py
```

Open:
- `http://127.0.0.1:5000`

## Running Tests

```bash
pytest -v
```

If you have multiple Python environments installed, use:

```bash
python -m pytest -v
```

## Deploying to Render (Web Service + Postgres)

### Render service settings

- **Build Command**:

```bash
pip install -r requirements.txt
```

- **Start Command**:

```bash
gunicorn run:app
```

### Environment variables on Render

- `DATABASE_URL` = Internal Database URL from your Render Postgres instance
- `SECRET_KEY` = strong random secret

### After first deploy

Run migrations and seed data in Render shell:

```bash
python -m flask --app run db upgrade
python -m app.scripts.seed
```

## Common Troubleshooting

### `ModuleNotFoundError: No module named 'psycopg2'`

Cause:
- Wrong requirements file installed, or dependency missing in deployed build.

Fix:
- Ensure Render installs root `requirements.txt`.

### `No such command 'db'`

Cause:
- App import failed before Flask-Migrate could initialize.

Fix:
- Resolve app import/runtime errors first, then run db commands again.

### Foreign key error while seeding articles

Cause:
- Articles inserted before users exist.

Fix:
- Use `python -m app.scripts.seed` (current script seeds users first).

## Notes

- Keep only one active requirements file for deployment consistency.
- For production, consider adding hashed passwords and stricter security settings.
