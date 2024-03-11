# Flask Application with Docker and Nginx

This project demonstrates how to dockerize a simple Flask application, set up a reverse proxy with Nginx, and write a script to parse data from the application.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker
- Docker Compose
- Python (if you want to run the data parsing script locally)

## Project Structure

- `app.py`: The Flask application.
- `requirements.txt`: Contains the Flask dependency.
- `Dockerfile`: Instructions for building the Docker image for the Flask application.
- `docker-compose.yml`: Configuration for running the Flask application and Nginx containers.
- `nginx.conf`: Configuration for the Nginx reverse proxy.
- `parse_data.py`: Script to retrieve and parse data from the Flask application.

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/lawrenceadmin/Devops_assignment.git
   cd Devops_assignment
```
## **Build and run the Docker containers**
```bash
docker-compose up --build
```
## Access the application:

Open your web browser and navigate to http://localhost. You should see the greeting message from the Flask application.
Visit http://localhost/data to see the sample JSON
## Run the data parsing script

In a separate terminal, run the following command
```bash
python parse_data.py
```
This will retrieve the data from the Flask application, parse it, and create text files in the files/ sub-directory.
## Check the output files
Verify that the text files have been created correctly in the files/ sub-directory.
## Clean Up
```bash
docker-compose down
```

