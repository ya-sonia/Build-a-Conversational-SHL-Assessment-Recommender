FROM python:3.11-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY catalog.py agent.py main.py ./
COPY tests/ ./tests/

EXPOSE 8000

# Use gunicorn for production; 2 workers fit within free-tier memory limits
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "60", "--access-logfile", "-"]