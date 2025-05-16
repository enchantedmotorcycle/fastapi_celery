# Python runtime as a parent image
FROM python:3.10-slim

# Install supervisor
RUN apt-get update && apt-get install -y supervisor && apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Copy the supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the port FastAPI will run on
EXPOSE 8080

# Command to start supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]