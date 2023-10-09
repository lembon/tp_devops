# syntax=docker/dockerfile:1
FROM python:3.11-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
# RUN apt-get update
RUN apk add --update --virtual .build-deps \
    build-base \
    postgresql-dev \
    python3-dev \
    libpq
# RUN apt-get install -y xmlsec1 libssl-dev libsasl2-dev libxml2-dev libxmlsec1-dev libxmlsec1-openssl
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY tp_devops_api/ /app/

