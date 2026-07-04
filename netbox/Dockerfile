FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/netbox

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    libpq-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
COPY base_requirements.txt .
COPY plugins.txt .

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r requirements.txt

RUN [ -f plugins.txt ] && pip install -r plugins.txt || true

COPY . .

EXPOSE 8080
