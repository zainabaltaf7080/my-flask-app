# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install selenium flask

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
