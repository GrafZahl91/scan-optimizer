FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    ghostscript \
    imagemagick \
    poppler-utils \
    unpaper \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/
COPY config/ /config/

CMD ["python", "optimizer.py"]
