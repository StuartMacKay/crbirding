# =============================================================================
# CRBirding Dockerfile
# =============================================================================
# Multi-stage build:
#   builder  - installs Python dependencies using uv
#   runtime  - lean final image
# =============================================================================

ARG PYTHON_VERSION=3.14

# -----------------------------------------------------------------------------
# Stage 1: Builder — installs dependencies
# -----------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /build

# Copy dependency files first (better layer caching)
COPY pyproject.toml uv.lock* ./

# Install dependencies into /opt/venv (outside /app so bind mounts don't overwrite it).
# Set DEV=1 at build time (e.g. via docker-compose build args) to include dev extras.
ARG DEV=0
RUN if [ "$DEV" = "1" ]; then \
        UV_PROJECT_ENVIRONMENT=/opt/venv uv sync --frozen --no-install-project; \
    else \
        UV_PROJECT_ENVIRONMENT=/opt/venv uv sync --frozen --no-dev --no-install-project; \
    fi

# -----------------------------------------------------------------------------
# Stage 2: Runtime
# -----------------------------------------------------------------------------
FROM python:${PYTHON_VERSION}-slim AS runtime

# Build arguments for UID/GID (can be overridden via docker-compose build args)
ARG UID=1000
ARG GID=1000

# Install runtime system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create the 'python' group and user with configurable UID/GID
RUN groupadd --gid ${GID} python \
    && useradd --uid ${UID} --gid python --shell /bin/bash --create-home python

# Copy the virtual environment from builder to /opt/venv (safe from bind mounts)
COPY --from=builder /opt/venv /opt/venv

# Set up the application directory
WORKDIR /app

# Copy application source
COPY --chown=python:python . .

# Copy and set up the entrypoint script
COPY --chown=python:python docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create directories needed at runtime
RUN mkdir -p /app/staticfiles /app/media \
    && chown -R python:python /app/staticfiles /app/media

# Switch to the non-root user
USER python

# Add the virtual environment to PATH
ENV PATH="/opt/venv/bin:$PATH"
ENV VIRTUAL_ENV=/opt/venv
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DJANGO_SETTINGS_MODULE=config.settings

# Expose the web server port
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn"]
