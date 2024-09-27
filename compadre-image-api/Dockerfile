# FROM python:3.11-slim-bookworm
# RUN apt update -y && apt install -y gcc g++
# WORKDIR /code

# RUN pip install --upgrade pip \
#     && pip install --no-cache-dir poetry
# COPY poetry.lock poetry.toml pyproject.toml ./
# # RUN poetry install
# RUN poetry config virtualenvs.create false && poetry install --no-root

# RUN mkdir -p /model

# COPY . /code/.

# RUN source .venv/bin/activate
# CMD poetry run gunicorn -c config/gunicorn_conf.py --workers $WORKERS --worker-class config.custom_uvicorn_worker.CustomUvicornWorker --bind 0.0.0.0:8000 app:app
FROM python:3.11-slim-bookworm

# Update and install system dependencies
RUN apt-get update -y && apt-get install -y gcc g++

# Set the working directory
WORKDIR /code

# Install Poetry
RUN pip install --upgrade pip && pip install poetry --no-cache-dir poetry

# Copy dependency files
COPY poetry.lock pyproject.toml ./

# Ensure Poetry creates the virtual environment in the container
ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

RUN poetry install --no-root

# Create necessary directories
RUN mkdir -p /model

COPY . /code/.

CMD ["sh", "-c", ". /code/.venv/bin/activate && poetry run gunicorn -c config/gunicorn_conf.py --workers 2 --worker-class config.custom_uvicorn_worker.CustomUvicornWorker --bind 0.0.0.0:8000 app:app"]