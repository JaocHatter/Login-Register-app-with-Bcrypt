FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/
COPY migrations /app/migrations/
COPY alembic.ini /app/alembic.ini 

ENV PYTHONPATH=/app
EXPOSE 5000

CMD ["flask", "--app", "src.app", "run", "--host=0.0.0.0"]