# Dockerfile for Vercel
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (cached layer)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose default HTTP port
EXPOSE 3000

# Use Uvicorn to run FastAPI
# Note: Vercel uses $PORT environment variable automatically if provided
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-3000}"]