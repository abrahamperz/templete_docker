FROM python:3.12.4-slim
LABEL authors="abrahamperz"

# Set up the working directory
WORKDIR /app

COPY requirements.txt /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Virtual env
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" PYTHONPATH=/app:$PYTHONPATH

RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt

COPY src /app/src
# COPY alembic /app/alembic
# COPY alembic.ini /app
COPY entrypoint.sh /app

RUN chmod +x /app/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]
