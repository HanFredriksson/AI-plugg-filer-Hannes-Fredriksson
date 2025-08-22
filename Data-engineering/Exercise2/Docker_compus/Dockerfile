# Use Python 3.11 base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Create folders for persistent data
RUN mkdir -p /app/data /app/src /app/data/generations

# Copy requirements if you have any
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src

# Default command to run your scraper
CMD ["python", "./src/pokemon_scraper.py"]