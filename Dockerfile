# Compile requirements first to take advantage of Docker layer caching
FROM python:3.11-slim as compile-requirements
WORKDIR /tmp
RUN pip install poetry
COPY pyproject.toml poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Build the actual image of the vigenaire app
FROM python:3.11-slim 
WORKDIR /code
COPY --from=compile-requirements /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]