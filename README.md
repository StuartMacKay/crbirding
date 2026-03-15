# CRBirding

A Django website for managing observations of colour-ringed birds.

## Overview

CRBirding allows birdwatchers and researchers to record and track sightings of individually colour-ringed birds. Each bird can be identified by its unique combination of colour rings, allowing movements and behaviour to be tracked over time.

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.14 |
| Framework | Django 6.0 |
| Database | PostgreSQL 17 |
| Cache / Broker | Redis 7 |
| Task Queue | Celery + Celery Beat |
| Static Files | Whitenoise |
| Web Server | Gunicorn |
| Object Storage | MinIO (S3-compatible) |
| Frontend | HTMX + Alpine.js + Tailwind CSS |
| Authentication | django-allauth |
| Monitoring | Sentry + django-health-check |
| Package Manager | uv |

## Quick Start

### Prerequisites

- Docker and Docker Compose
- `make`

### 1. Clone and configure

```bash
cp .env.example .env
# Edit .env with your settings
```

### 2. Build and start

```bash
make build
make up
```

### 3. Run migrations and create a superuser

```bash
make migrate
make createsuperuser
```

### 4. Open the site

- Web app: http://localhost:8000
- Admin: http://localhost:8000/admin/
- Health check: http://localhost:8000/health/
- MinIO console: http://localhost:9001

## Development

### Running tests

```bash
make test          # Full suite with coverage
make test-fast     # No coverage (faster)
make test-core     # Core app only
make test-accounts # Accounts app only
```

### Code quality

```bash
make lint          # Run ruff linter
make format        # Run ruff formatter
make typecheck     # Run ty type checker
make check         # Run all checks (no fixes)
```

### Django shell

```bash
make shell   # Opens shell_plus (IPython)
make bash    # Opens bash in the web container
make dbshell # Opens psql
```

### Development-only endpoints

In `development` mode, the following endpoints are available for testing:

| URL | Description |
|-----|-------------|
| `/403/` | Test 403 Forbidden page |
| `/404/` | Test 404 Not Found page |
| `/500/` | Test 500 Server Error page |
| `/sentry-test/` | Trigger a Sentry test error |
| `/__reload__/` | Browser auto-reload (django-browser-reload) |
| `/__debug__/` | Django Debug Toolbar |

## Project Structure

```
crbirding/
├── apps/                    # Django applications
│   ├── core/                # Home page, error handlers
│   └── accounts/            # User authentication & management
├── assets/
│   ├── static/              # Static files (CSS, JS, images)
│   └── templates/           # Django templates
├── config/                  # Django configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── celery.py
├── docker/
│   └── entrypoint.sh        # Docker entrypoint script
├── .data/                   # Named Docker volumes (gitignored)
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── pyproject.toml
└── Makefile
```

## Environment Variables

See `.env.example` for all available environment variables with descriptions.

Key variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `DJANGO_ENV` | `development` | `development` or `production` |
| `SECRET_KEY` | (insecure default) | Django secret key |
| `DB_HOST` | `db` | PostgreSQL host |
| `REDIS_URL` | `redis://redis:6379/0` | Redis URL |
| `USE_S3` | `False` | Enable S3/MinIO storage |
| `SENTRY_DSN` | (empty) | Sentry DSN for error tracking |

## Database Backup & Restore

```bash
make backup                         # Create a timestamped backup
make restore FILE=.data/backups/... # Restore from a backup file
make list-backups                   # List available backups
```

## Deployment

The application is designed to be deployed to a VPS (e.g., a DigitalOcean Droplet) using Docker Compose.

For production:
1. Set `DJANGO_ENV=production` in your `.env`
2. Set a strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for your domain
4. Enable HTTPS and set `SECURE_SSL_REDIRECT=True`
5. Configure a real SMTP server for email
6. Set `SENTRY_DSN` for error tracking

## Favicon Generation

The favicon PNG files are placeholders. Generate proper ones from `assets/static/img/logo.svg`:

```bash
# Using Inkscape:
for size in 16 32 48 192 512; do
  inkscape assets/static/img/logo.svg \
    --export-png=assets/static/img/favicon-${size}x${size}.png \
    --export-width=${size} --export-height=${size}
done

# Or using ImageMagick:
for size in 16 32 48 192 512; do
  convert -background none assets/static/img/logo.svg \
    -resize ${size}x${size} \
    assets/static/img/favicon-${size}x${size}.png
done
```

## Licence

MIT
