# Django REST API - UserProfile Management System

## About

This is a User Profile Management REST API developed using Django and Django REST Framework (DRF).

The project allows authenticated users to:
- Create user profiles
- View user profiles
- Update user profiles
- Delete user profiles


## Features

- User Authentication
- CRUD Operations
- Custom Permission
- Search by title and content
- Order by ID
- Pagination (5 posts per page)

## Technologies Used

- Python 3
- Django 6.0.1
- Django REST Framework
- django-filter
- SQLite3

## How to Run

1. Create a virtual environment

```
python -m venv venv
```

2. Activate the virtual environment

```
venv\Scripts\activate
```

3. Install required packages

```
pip install django==6.0.1
pip install djangorestframework
pip install django-filter
```

4. Run migrations

```
python manage.py migrate
```

5. Start the server

```
python manage.py runserver
```

## Author

Garima
