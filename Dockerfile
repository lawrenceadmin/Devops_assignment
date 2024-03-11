# Use an official Python runtime as a parent image
FROM python:3.9-slim
# Set the working directory inside  the container
WORKDIR /app
# copy & Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the current directory contents into the container at /app
COPY app.py .
# Define environment variable
ENV GREETING="Hello, World!"
# Make port 5000 available outside this container
EXPOSE 5000
# Run app.py when the container launches
CMD ["python", "app.py"]
