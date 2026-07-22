# DevOps Flask Project

A simple Flask application containerized with Docker, built as part of learning DevOps and AWS deployment practices.

## Stack
- Python / Flask
- Gunicorn (production WSGI server)
- Docker

## Run locally
docker build -t devops-project .
docker run -d -p 5000:5000 --name devops-app devops-project
