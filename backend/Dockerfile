# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run migrations (optional) and start Gunicorn server
CMD ["gunicorn", "ticketing_system.wsgi:application", "--bind", "0.0.0.0:8000"]
