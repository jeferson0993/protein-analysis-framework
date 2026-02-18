# ---------- Stage 1: Builder ----------
FROM python:3.10-slim AS builder

WORKDIR /install

COPY requirements.txt .
RUN pip install --prefix=/install/deps -r requirements.txt


# ---------- Stage 2: Runtime ----------
FROM python:3.10-slim

LABEL maintainer="Scientific Protein Framework"

WORKDIR /app

COPY --from=builder /install/deps /usr/local
COPY app/ /app/

RUN mkdir -p /app/data /app/results /app/logs

ENTRYPOINT ["python", "cli.py"]
