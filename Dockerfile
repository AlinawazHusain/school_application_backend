FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Vercel default port
EXPOSE 3000

# Run FastAPI with $PORT fallback
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-3000}"]