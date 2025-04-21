# Dockerfile.backend
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY data /app/data
EXPOSE 2000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2000"]
