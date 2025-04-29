FROM python:3.12.4-slim
LABEL authors="abrahamperz"

# Set up the working directory
WORKDIR /app/backend

COPY requirements.txt /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Virtual env
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" PYTHONPATH=/app:$PYTHONPATH

RUN pip install --upgrade pip &&  \
    pip install -r /app/requirements.txt

COPY backend/src /app/backend/src
# COPY alembic /app/backend/alembic
# COPY alembic.ini /app/backend
COPY entrypoint.sh /app/backend

RUN chmod +x /app/backend/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/app/entrypoint.sh"]
