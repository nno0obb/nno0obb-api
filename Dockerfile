FROM python:3.12-slim AS builder
ENV PYTHONUNBUFFERED=1
WORKDIR /

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
COPY pyproject.toml poetry.lock ./
RUN poetry install

FROM python:3.12-slim
WORKDIR /
COPY --from=builder .venv .venv
COPY . .
CMD ["source", ".venv/bin/activate", "&&", "python3", "main.py"]
