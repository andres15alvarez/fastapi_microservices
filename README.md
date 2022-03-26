# Microservices with FastAPI
Two microservices made with FastAPI connected to the same RedisJSON instance.
These microservices communicate each other through HTTP.
Each folder is a microservice.

## Setup
In each folder:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
In the other microservice:
```
uvicorn main:app --reload --port 8001