FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS app

WORKDIR /app
COPY . .

ENV UV_LINK_MODE copy
ENV UV_PROJECT_ENVIRONMENT /run/app/.venv
RUN uv sync --extra dev

ENV PYTHONPATH /app/src:/app/tests
ENV MYPYPATH /app/src:/app/tests

ENV WATCHFILES_FORCE_POLLING true

ENTRYPOINT ["bash", "deployments/dev/backend/entrypoint.sh"]
