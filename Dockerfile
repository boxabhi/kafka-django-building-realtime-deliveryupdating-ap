# Use the official Python image from the Docker Hub
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    build-base \
    netcat-openbsd \
    openssl-dev \
    cyrus-sasl-dev \
    curl \
    make \
    bash

# Install librdkafka from source
RUN curl -L "https://github.com/edenhill/librdkafka/archive/refs/tags/v2.5.0.tar.gz" -o librdkafka.tar.gz && \
    tar -xzf librdkafka.tar.gz && \
    cd librdkafka-2.5.0 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf librdkafka-2.5.0 librdkafka.tar.gz

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code
COPY . /app/

# Run Django migrations and start the server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
