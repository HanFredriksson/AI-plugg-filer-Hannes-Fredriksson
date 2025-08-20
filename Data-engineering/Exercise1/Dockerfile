# Base image
FROM python:3.9-slim

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /Exercise1

# Copy project files
COPY requirements.txt ./
COPY src/ src/
COPY logs/ logs/
COPY mycron /etc/cron.d/mycron

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/mycron

# Apply cron job
RUN crontab /etc/cron.d/mycron

# Ensure logs folder exists
RUN mkdir -p /Exercise1/logs && touch /Exercise1/logs/cron.log

# Run cron in the foreground
CMD ["cron", "-f"]
