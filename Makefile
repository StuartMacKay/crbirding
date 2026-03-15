# =============================================================================
# CRBirding Makefile
# =============================================================================
# Usage: make <target>
# Run `make help` to see all available targets.
# =============================================================================

.PHONY: help build up down restart logs shell dbshell \
        migrate makemigrations showmigrations \
        test lint format typecheck \
        collectstatic createsuperuser \
        backup restore \
        clean prune

# Default target
.DEFAULT_GOAL := help

# Docker Compose command
DC := docker compose

# Container names
WEB_SERVICE := web
DB_SERVICE  := db

# Colours for output
CYAN  := \033[0;36m
GREEN := \033[0;32m
RESET := \033[0m

# ---------------------------------------------------------------------------
# Help
# ---------------------------------------------------------------------------
help: ## Show this help message
	@echo ""
	@echo "  CRBirding — available make targets"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ { printf "  $(CYAN)%-20s$(RESET) %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""

# ---------------------------------------------------------------------------
# Docker lifecycle
# ---------------------------------------------------------------------------
build: ## Build all Docker images
	$(DC) build

build-no-cache: ## Build all Docker images without cache
	$(DC) build --no-cache

up: ## Start all services in the background
	$(DC) up -d

up-web: ## Start only the web service and its dependencies
	$(DC) up -d web

down: ## Stop all services
	$(DC) down

restart: ## Restart all services
	$(DC) restart

restart-web: ## Restart only the web service
	$(DC) restart $(WEB_SERVICE)

# ---------------------------------------------------------------------------
# Logs
# ---------------------------------------------------------------------------
logs: ## Tail logs for all services
	$(DC) logs -f

logs-web: ## Tail logs for the web service
	$(DC) logs -f $(WEB_SERVICE)

logs-worker: ## Tail logs for the Celery worker
	$(DC) logs -f worker

logs-beat: ## Tail logs for Celery beat
	$(DC) logs -f beat

logs-db: ## Tail logs for the database
	$(DC) logs -f $(DB_SERVICE)

# ---------------------------------------------------------------------------
# Shells
# ---------------------------------------------------------------------------
shell: ## Open a Django shell (shell_plus) in the web container
	$(DC) run --rm $(WEB_SERVICE) manage shell_plus

bash: ## Open a bash shell in the web container
	$(DC) run --rm $(WEB_SERVICE) bash

dbshell: ## Open a PostgreSQL shell
	$(DC) exec $(DB_SERVICE) psql -U $${DB_USER:-crbirding} -d $${DB_NAME:-crbirding}

redis-cli: ## Open a Redis CLI session
	$(DC) exec redis redis-cli

# ---------------------------------------------------------------------------
# Database migrations
# ---------------------------------------------------------------------------
migrate: ## Run database migrations
	$(DC) run --rm $(WEB_SERVICE) manage migrate

makemigrations: ## Create new database migrations
	$(DC) run --rm $(WEB_SERVICE) manage makemigrations

makemigrations-empty: ## Create an empty migration for the given app (usage: make makemigrations-empty APP=myapp)
	$(DC) run --rm $(WEB_SERVICE) manage makemigrations --empty $(APP)

showmigrations: ## Show all migrations and their status
	$(DC) run --rm $(WEB_SERVICE) manage showmigrations

squashmigrations: ## Squash migrations (usage: make squashmigrations APP=myapp FROM=0001)
	$(DC) run --rm $(WEB_SERVICE) manage squashmigrations $(APP) $(FROM)

# ---------------------------------------------------------------------------
# Static files
# ---------------------------------------------------------------------------
collectstatic: ## Collect static files
	$(DC) run --rm $(WEB_SERVICE) manage collectstatic --noinput

# ---------------------------------------------------------------------------
# Superuser
# ---------------------------------------------------------------------------
createsuperuser: ## Create a Django superuser
	$(DC) run --rm $(WEB_SERVICE) manage createsuperuser

# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
test: ## Run the full test suite with coverage
	$(DC) run --rm -e DJANGO_ENV=development $(WEB_SERVICE) python -m pytest

test-fast: ## Run tests without coverage (faster)
	$(DC) run --rm -e DJANGO_ENV=development $(WEB_SERVICE) python -m pytest --no-cov

test-core: ## Run only the core app tests
	$(DC) run --rm -e DJANGO_ENV=development $(WEB_SERVICE) python -m pytest apps/core/tests.py

test-accounts: ## Run only the accounts app tests
	$(DC) run --rm -e DJANGO_ENV=development $(WEB_SERVICE) python -m pytest apps/accounts/tests.py

test-file: ## Run a specific test file (usage: make test-file FILE=apps/core/tests.py)
	$(DC) run --rm -e DJANGO_ENV=development $(WEB_SERVICE) python -m pytest $(FILE)

# ---------------------------------------------------------------------------
# Code quality
# ---------------------------------------------------------------------------
lint: ## Run ruff linter
	$(DC) run --rm $(WEB_SERVICE) python -m ruff check .

lint-fix: ## Run ruff linter and auto-fix issues
	$(DC) run --rm $(WEB_SERVICE) python -m ruff check --fix .

format: ## Run ruff formatter
	$(DC) run --rm $(WEB_SERVICE) python -m ruff format .

format-check: ## Check formatting without making changes
	$(DC) run --rm $(WEB_SERVICE) python -m ruff format --check .

typecheck: ## Run ty type checker
	$(DC) run --rm $(WEB_SERVICE) python -m ty check .

# Run all quality checks
check: lint format-check ## Run all code quality checks (no fixes)

# ---------------------------------------------------------------------------
# Database backup & restore
# ---------------------------------------------------------------------------
backup: ## Backup the database to .data/backups/ (usage: make backup)
	@mkdir -p .data/backups
	@TIMESTAMP=$$(date +%Y%m%d_%H%M%S); \
	BACKUP_FILE=".data/backups/crbirding_$${TIMESTAMP}.sql.gz"; \
	$(DC) exec -T $(DB_SERVICE) pg_dump \
		-U $${DB_USER:-crbirding} \
		-d $${DB_NAME:-crbirding} \
		| gzip > "$${BACKUP_FILE}"; \
	echo "$(GREEN)Backup saved to $${BACKUP_FILE}$(RESET)"

restore: ## Restore database from a backup file (usage: make restore FILE=.data/backups/crbirding_20240101_120000.sql.gz)
	@if [ -z "$(FILE)" ]; then \
		echo "Error: FILE is required. Usage: make restore FILE=path/to/backup.sql.gz"; \
		exit 1; \
	fi
	@echo "Restoring database from $(FILE)..."
	@gunzip -c $(FILE) | $(DC) exec -T $(DB_SERVICE) psql \
		-U $${DB_USER:-crbirding} \
		-d $${DB_NAME:-crbirding}
	@echo "$(GREEN)Database restored from $(FILE)$(RESET)"

list-backups: ## List available database backups
	@ls -lh .data/backups/ 2>/dev/null || echo "No backups found in .data/backups/"

# ---------------------------------------------------------------------------
# Cleanup
# ---------------------------------------------------------------------------
clean: ## Remove Python cache files and build artefacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	rm -rf .pytest_cache htmlcov .coverage coverage.xml .ruff_cache

prune: ## Remove stopped containers, unused images and volumes (CAUTION: removes data)
	$(DC) down --volumes --remove-orphans
	docker system prune -f

# ---------------------------------------------------------------------------
# Pre-commit
# ---------------------------------------------------------------------------
pre-commit-install: ## Install pre-commit hooks
	$(DC) run --rm $(WEB_SERVICE) pre-commit install

pre-commit-run: ## Run pre-commit on all files
	$(DC) run --rm $(WEB_SERVICE) pre-commit run --all-files

# ---------------------------------------------------------------------------
# MinIO bucket setup
# ---------------------------------------------------------------------------
minio-setup: ## Create the default MinIO bucket
	@echo "Creating MinIO bucket '$(shell grep AWS_STORAGE_BUCKET_NAME .env 2>/dev/null | cut -d= -f2 || echo crbirding)'..."
	$(DC) run --rm \
		-e MC_HOST_minio=http://$${AWS_ACCESS_KEY_ID:-minioadmin}:$${AWS_SECRET_ACCESS_KEY:-minioadmin}@minio:9000 \
		--entrypoint="" \
		minio/mc mb --ignore-existing minio/$${AWS_STORAGE_BUCKET_NAME:-crbirding}
