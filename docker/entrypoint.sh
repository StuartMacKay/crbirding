#!/usr/bin/env bash
# =============================================================================
# Docker entrypoint script for crbirding
# =============================================================================
set -euo pipefail

# Activate the virtual environment
source /opt/venv/bin/activate

# Colours for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No colour

log() {
  echo -e "${GREEN}[entrypoint]${NC} $*"
}

warn() {
  echo -e "${YELLOW}[entrypoint]${NC} $*"
}

error() {
  echo -e "${RED}[entrypoint]${NC} $*" >&2
}

# ---------------------------------------------------------------------------
# Wait for the database to be ready
# ---------------------------------------------------------------------------
wait_for_db() {
  local host="${DB_HOST:-db}"
  local port="${DB_PORT:-5432}"
  local max_retries=30
  local retry=0

  log "Waiting for database at ${host}:${port}..."

  while ! python -c "
import sys, socket
try:
    s = socket.create_connection(('${host}', ${port}), timeout=2)
    s.close()
    sys.exit(0)
except Exception:
    sys.exit(1)
" 2>/dev/null; do
    retry=$((retry + 1))
    if [ "$retry" -ge "$max_retries" ]; then
      error "Database at ${host}:${port} did not become available after ${max_retries} retries."
      exit 1
    fi
    warn "Database not ready (attempt ${retry}/${max_retries}), retrying in 2s..."
    sleep 2
  done
  log "Database is ready."
}

# ---------------------------------------------------------------------------
# Wait for Redis to be ready
# ---------------------------------------------------------------------------
wait_for_redis() {
  local url="${REDIS_URL:-redis://redis:6379/0}"
  # Extract host and port from URL
  local host
  host=$(python -c "from urllib.parse import urlparse; u=urlparse('${url}'); print(u.hostname)")
  local port
  port=$(python -c "from urllib.parse import urlparse; u=urlparse('${url}'); print(u.port or 6379)")
  local max_retries=30
  local retry=0

  log "Waiting for Redis at ${host}:${port}..."

  while ! python -c "
import sys, socket
try:
    s = socket.create_connection(('${host}', ${port}), timeout=2)
    s.close()
    sys.exit(0)
except Exception:
    sys.exit(1)
" 2>/dev/null; do
    retry=$((retry + 1))
    if [ "$retry" -ge "$max_retries" ]; then
      error "Redis at ${host}:${port} did not become available after ${max_retries} retries."
      exit 1
    fi
    warn "Redis not ready (attempt ${retry}/${max_retries}), retrying in 2s..."
    sleep 2
  done
  log "Redis is ready."
}

# ---------------------------------------------------------------------------
# Main entry point logic
# ---------------------------------------------------------------------------
CMD="${1:-gunicorn}"

case "$CMD" in
  gunicorn)
    wait_for_db
    wait_for_redis

    log "Running database migrations..."
    python manage.py migrate --noinput

    log "Collecting static files..."
    python manage.py collectstatic --noinput

    log "Starting Gunicorn..."
    exec gunicorn config.wsgi:application \
      --bind "0.0.0.0:${PORT:-8000}" \
      --workers "${GUNICORN_WORKERS:-4}" \
      --worker-class "${GUNICORN_WORKER_CLASS:-gthread}" \
      --threads "${GUNICORN_THREADS:-2}" \
      --timeout "${GUNICORN_TIMEOUT:-120}" \
      --keep-alive "${GUNICORN_KEEP_ALIVE:-5}" \
      --access-logfile - \
      --error-logfile - \
      --log-level "${GUNICORN_LOG_LEVEL:-info}"
    ;;

  celery-worker)
    wait_for_db
    wait_for_redis

    log "Starting Celery worker..."
    exec celery -A config worker \
      --loglevel="${CELERY_LOG_LEVEL:-info}" \
      --concurrency="${CELERY_CONCURRENCY:-4}" \
      --hostname="worker@%h"
    ;;

  celery-beat)
    wait_for_db
    wait_for_redis

    log "Starting Celery beat scheduler..."
    exec celery -A config beat \
      --loglevel="${CELERY_LOG_LEVEL:-info}" \
      --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ;;

  migrate)
    wait_for_db
    log "Running database migrations..."
    exec python manage.py migrate --noinput
    ;;

  collectstatic)
    log "Collecting static files..."
    exec python manage.py collectstatic --noinput
    ;;

  shell)
    wait_for_db
    exec python manage.py shell_plus
    ;;

  manage)
    shift
    exec python manage.py "$@"
    ;;

  bash)
    exec /bin/bash
    ;;

  *)
    # Pass through any other commands
    exec "$@"
    ;;
esac
