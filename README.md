# 🚗 Travel Booking API using Django REST Framework

A RESTful Travel Booking backend API built with Django & Django REST Framework — implements endpoints for browsing travel options and managing bookings, fully documented with Swagger.

This backend is suitable for integration with a frontend (mobile or web) and serves as a clean, deploy-ready portfolio project.

## 🧩 Key Features

📌 REST API with clean endpoints

🔐 Authentication supported (token/JWT if implemented)

📖 Swagger UI for interactive documentation

🗺️ Booking management

🧠 Built on scalable Django + DRF architecture

## 🛠️ Ready to integrate with frontend or mobile apps

## 🛠️ Tech Stack

Technology	Purpose
Python	Backend language
Django	Web framework
Django REST Framework	API development
Swagger (drf-yasg or similar)	API documentation
SQLite (Dev)	Database (replace for production)

## 📁 Project Structure (Simplified)
Travel_booking_API_using_drf/
├── bookings/                 # Booking app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── core/                     # Core Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3                # *Should be .gitignored* 🚫
└── schema.yml

## 🚀 Installation

Run this locally:
Clone repo

### git clone https://github.com/SandeepR8/Travel_booking_API_using_drf.git
cd Travel_booking_API_using_drf
Create & activate Python virtual environment

python -m venv venv

### Windows
venv\Scripts\activate

### Linux/Mac
source venv/bin/activate


### Install dependencies

pip install -r requirements.txt

Apply migrations

python manage.py migrate

Run server

python manage.py runserver

## 📜 API Documentation (Swagger)

Access your API documentation in the browser:

UI	Path
Swagger UI	http://127.0.0.1:8000/api/schema/swagger-ui/
ReDoc (if enabled)	http://127.0.0.1:8000/api/schema/redoc/

Swagger gives you live testing, request/response details, and auth info — it’s the best way for someone to explore your API. 
Horilla Open Source HR Software

### 🧠 Authentication :
Register / Login endpoint returns token

Use token in request headers:

Authorization: Bearer <your_token>

If not implemented yet — consider adding JWT Authentication (industry standard).

### 🗂️ Common Endpoints
Method	Endpoint	Description

POST api/BusDetails/ creating the bus details (AdminUser only)
POST api/buses/ list of buses 
GET api/user-bookings/ Get the specific user booking
POST	/api/bookings/	Create a booking
GET	/api/bookings/<id>/	Retrieve booking
PATCH	/api/bookings/<id>/	Update booking
DELETE	/api/bookings/<id>/	Cancel booking
