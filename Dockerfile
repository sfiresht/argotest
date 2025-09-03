# Dockerfile
# This Dockerfile builds an image for your Python Flask application.

# Use an official Python runtime as a parent image
FROM python:3.9-slim-bullseye
# Set the working directory in the container
WORKDIR /app
RUN chmod -R 7777 /app


# Install any needed packages specified in requirements.txt
# Also install 'procps' for 'ps' command, 'vim' for editing, and 'iputils-ping' for ping.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    procps \
    vim \
    iputils-ping && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#USER default
# Copy the application code into the container at /app
COPY app.py .
RUN chmod 777 app.py

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

