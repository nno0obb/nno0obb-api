# Builder Stage
FROM python:3.12-slim AS builder
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --upgrade pip poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-interaction
COPY app app

# Runtime Stage
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY app app
CMD ["python3", "app/main.py"]
