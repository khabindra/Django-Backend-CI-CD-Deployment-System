# Use an official, lightweight Python image
FROM python:3.12-slim

# Set environment variables to ensure Python outputs everything immediately
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory inside the container 
WORKDIR /app

# Install system dependencies (required for PostgreSQL)
RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first (for caching )
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code 
COPY . /app/

# Expose the port Django will run on 
EXPOSE 8000

# Command to run the application 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

