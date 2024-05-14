FROM python:3.11.5-slim-bookworm
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev
COPY ./todo_app ./todo_app
EXPOSE 5000
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]