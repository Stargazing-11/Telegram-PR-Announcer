# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
# Python won't try to write .pyc files on the import of source modules
ENV PYTHONDONTWRITEBYTECODE 1
# Python outputs everything to terminal without buffering
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
