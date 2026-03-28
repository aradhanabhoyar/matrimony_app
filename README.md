# Matrimony Backend API (Tornado + Python)

## Overview

This project is a backend system for a matrimony platform where users can:

* Register and login securely
* Create, update, and delete their profiles
* Search for potential matches

The backend is built using **Python Tornado framework** with **SQLAlchemy ORM** and **JWT-based authentication**.


## Project Structure

matrimony_app/
│
├── app.py
├── routes.py
│
├── handlers/
│   ├── user_handler.py
│   ├── profile_handler.py
│
├── models/
│   ├── user_model.py
│   ├── profile_model.py
│
├── utils/
│   ├── db.py
│   ├── auth.py
│   ├── response.py
│   ├── middleware.py


## Setup Instructions

### 1. Clone Repository
git clone 
cd matrimony_app

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   (Windows)

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run Application
python app.py


Server will start at:
http://localhost:8888


## Database

* Uses **SQLite** database (`matrimony.db`)
* Tables are auto-created on server start

## Authentication

* Uses **JWT (JSON Web Tokens)**
* Token must be passed in header:
Authorization: Bearer <token>


## API Documentation

### 1. Register User

**POST** `/register`

#### Request:

json
{
  "name": "Punam",
  "email": "punam@gmail.com",
  "password": "123456"
}


#### Response:

json
{
  "status": "success",
  "message": "User registered",
  "data": null
}


### 2. Login User

**POST** `/login`

#### Request:

json
{
  "email": "punam@gmail.com",
  "password": "123456"
}


#### Response:

json
{
  "status": "success",
  "message": "Login successful",
  "data": {
    "token": "JWT_TOKEN"
  }
}


### 3. Create Profile

**POST** `/profile`

#### Headers:
Authorization: Bearer <token>


#### Request:

json
{
  "age": 26,
  "gender": "female",
  "religion": "hindu",
  "city": "Pune"
}


#### Response:

json
{
  "status": "success",
  "message": "Profile created",
  "data": null
}

### 4. Update Profile

**PUT** `/profile`

#### Headers:
Authorization: Bearer <token>

#### Request:

json
{
  "age": 27,
  "city": "Mumbai"
}

#### Response:

json
{
  "status": "success",
  "message": "Profile updated",
  "data": null
}


### 5. Delete Profile

**DELETE** `/profile`

#### Headers:
Authorization: Bearer <token>

#### Response:

json
{
  "status": "success",
  "message": "Profile deleted",
  "data": null
}

### 6. Search Profiles

**GET** `/search`

#### Example:

/search?city=Pune&age_min=20&age_max=30


#### Response:

json
{
  "status": "success",
  "message": "Profiles fetched",
  "data": [
    {
      "age": 26,
      "city": "Pune",
      "religion": "hindu"
    }
  ]
}


## CRUD Operations Supported

* Create → Register, Profile creation
* Read → Search profiles
* Update → Update profile
* Delete → Delete profile

This ensures full CRUD functionality for user profiles.

## Security Practices

* Password hashing using **bcrypt**
* JWT authentication with expiry
* Input validation
* Protected routes using middleware

## Error Handling

Standard error response format:

json
{
  "status": "error",
  "message": "Error message"
}

HTTP status codes:

* 400 → Bad Request
* 401 → Unauthorized
* 500 → Internal Server Error

##  Assumptions Made

* Each user has only one profile
* Email must be unique
* SQLite is sufficient for development
* Basic filtering is enough for matchmaking
* Profile can be updated or deleted only by the owner
* No frontend included (API-only system)

## Future Improvements

* Add matchmaking algorithm
* Use PostgreSQL for production
* Add pagination for search
* Add email verification
* Add GET `/profile` (view own profile)
* Add user preferences & matching score

##  Author

**Aradhana Bhoyar**

## Conclusion

This project demonstrates:

* Clean backend architecture
* REST API design
* Authentication & security
* Database integration
* Full CRUD implementation


