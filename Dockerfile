# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.8.3

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get clean

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set work directory
WORKDIR /code

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy project
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Run Daphne ASGI server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

