# Use Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Redis client library and Flask
RUN pip install redis flask

# Run the Flask app
CMD ["python", "./app.py"]