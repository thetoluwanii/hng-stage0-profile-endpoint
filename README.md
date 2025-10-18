# Cat Profile API

A simple Django REST API that returns my profile information along with a dynamic cat fact fetched from the Cat Facts API
.
This project is my submission for HNG Internship Backend Stage 0.

Live Demo

Base URL:
https://web-production-34b8f.up.railway.app

Profile Endpoint:
https://web-production-34b8f.up.railway.app/me/

# Project Overview

The API exposes a single GET /me endpoint that returns JSON data in this format:

{
  "status": "success",
  "user": {
    "email": "gracetoluwanii@gmail.com",
    "name": "Omojunikanbi Toluwanimi Grace",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-17T12:34:56.789Z",
  "fact": "Cats can rotate their ears 180 degrees."
}

## Features

1. Returns structured JSON response

2. Dynamic UTC timestamp (ISO 8601 format)

3. Fetches a new random cat fact from Cat Fact Ninja API

4. Handles network errors gracefully

5. Fully deployed on Railway

## Tech Stack

Language: Python 3.13

Framework: Django 5.x

Server: Gunicorn

Deployment: Railway

## How to Run Locally
1. Clone the repository

git clone https://github.com/<thetoluwanii>/catprofile.git
cd catprofile

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Run the server
python manage.py runserver


Visit http://127.0.0.1:8000/me to test locally.

## Deployment Notes

This project uses:

-- Gunicorn as the WSGI server

-- Whitenoise for static file management

-- Railway.app for hosting


## Environment Variables

No environment variables are required for this project.

Author

Omojunikanbi Toluwanimi Grace
Email: gracetoluwanii@gmail.com

Backend Developer — Python/Django

HNG Backend Stage 0

This project demonstrates:

RESTful API design and JSON formatting

Integration with a third-party API

Dynamic timestamp generation

Deployment to a live server
