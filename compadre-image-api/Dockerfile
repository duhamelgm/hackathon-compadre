FROM python:3.11-slim-bookworm
RUN apt update -y && apt install -y gcc g++
WORKDIR /code

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install

RUN mkdir -p /model

COPY . /code/.

CMD poetry run gunicorn -c config/gunicorn_conf.py --workers $WORKERS --worker-class config.custom_uvicorn_worker.CustomUvicornWorker --bind 0.0.0.0:8000 app:app
