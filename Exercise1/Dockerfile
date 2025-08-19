# Base image python3.9
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /Exercise1

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Run script when container starts
CMD ["python", "src/ex1_0_setup.py"]