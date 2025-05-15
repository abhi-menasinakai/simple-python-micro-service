# Use an official Python base image
FROM python:3.10-alpine

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1

# Working directory
WORKDIR /app

# Copy files
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt


# Add a non-root user and switch to it
RUN adduser --disabled-password --gecos '' appuser
USER appuser


# Copy the application code
COPY . .

# Expose the port 
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]

