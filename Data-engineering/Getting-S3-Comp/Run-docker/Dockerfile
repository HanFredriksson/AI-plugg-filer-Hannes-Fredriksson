# Base image
FROM python:3.9-slim

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /Run-docker

# Copy project files
COPY requirements.txt ./
COPY src/ src/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run S3 test in the foreground
CMD ["python", "*./main.py"]
