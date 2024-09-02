# Install build tools and dependencies
FROM python:3.11.5-slim-bookworm as base
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

# Copy application code
COPY ./todo_app ./todo_app
EXPOSE 5000

# Production
FROM base as production
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

# Development
FROM base as development
ENV FLASK_DEBUG=1
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
