# FastAPI Project (Ecommerce Backend)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Prerequisites](#Prerequisites)
- [Clone the Repository](#Clone-the-Repository)
- [Create a Virtual Environment](#Create-a-Virtual-Environment)
- [Activate the Virtual Environment](#Activate-the-Virtual-Environment)
- [Install the Required Dependencies](#Install-the-Required-Dependencies)
- [Create a .env file in the root directory and add the following variables:](#Create-a-.env-file-in-the-root-directory-and-add-the-following-variables)
- [Run the Application](#Run-the-Application)
- [API Endpoints](#API-Endpoints)
- [Running Tests](#Running-Tests)
- [My Intuition for this task](#My-Intuition-for-this-task)
- [My assumptions](#My-assumptions)




## Introduction
This project is a backend application built with FastAPI. It allows users to upload and retrieve files through a RESTful API via proper encryption of [fernet](https://cryptography.io/en/latest/fernet/)

## Features
- File upload
- File retrieval
- Database integration with Tortoise ORM

## Installation
To get started with the project, follow these steps:

### Prerequisites
- Python 3.9 or higher
- PostgreSQL (for development purposes)

### Clone the Repository
```bash
git clone https://github.com/sujanMidatani7/ecom-api-backend-934729.git
cd ecom-api-backend-934729
```
### Create a Virtual Environment
```bash
python -m venv venv
```
### Activate the Virtual Environment
```bash
# Windows
venv\Scripts\activate
# Linux
source venv/bin/activate
```
### Install the Required Dependencies
```bash
pip install -r requirements.txt
```
### Create a .env file in the root directory and add the following variables:
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/yourdatabase
SECRET_KEY=your_secret_key
```

### Run the Application
```bash
uvicorn app.main:app --reload
```
## API Endpoints
The API endpoints are documented using Swagger UI. To access the documentation, visit `http://localhost:8000/docs` 

## If you want to run via docker container
```bash
docker-compose up
```

## Running Tests
To run the tests, execute the following command:
```bash
pytest
```

## My Intuition for this task
- I have used FastAPI for this task because it is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is easy to use and has a lot of features that make it a great choice for building APIs.
- I have used Tortoise ORM for database integration because it is an easy-to-use asyncio ORM inspired by Django. It is built on top of databases and is designed to work with async/await.
- I have used Pydantic for data validation because it is a data validation library that uses Python type annotations. It is easy to use and provides a lot of features for data validation.
- I have used Fernet for encryption because it is a symmetric encryption algorithm that is easy to use and provides a high level of security. It is based on the AES encryption algorithm and provides a secure way to encrypt and decrypt data.
- I have used Docker for containerization because it is a great way to package applications and their dependencies into a single container that can be run on any platform. It provides a lightweight and portable way to run applications in a consistent environment.
- I have used pytest for testing because it is a powerful testing framework that makes it easy to write and run tests. It provides a lot of features for testing and is easy to use.

### My assumptions
- I have assumed that the files uploaded by the users are small in size and can be stored in the database. If the files are large in size, it is better to store them in a file storage service like Amazon S3 or Google Cloud Storage.
- I have assumed that the users will upload files in a secure way and that the files will be encrypted before being stored in the database. This is to ensure that the files are secure and cannot be accessed by unauthorized users.
- I have assumed that the users will provide valid data when uploading files and that the data will be validated before being processed. This is to ensure that the data is correct and that the application works as expected.
- I have assumed that the response for the post method contains id of the perticular file stored in db and the static location of it in the application






