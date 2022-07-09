FROM python:3.10-bullseye AS poetry

RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock .
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.10-bullseye
WORKDIR /app
COPY --from=poetry /app/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
