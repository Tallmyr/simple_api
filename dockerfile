FROM python:3.10-bullseye AS poetry
RUN pip install poetry
WORKDIR /code
COPY pyproject.toml poetry.lock .
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.10-bullseye
WORKDIR /app
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
