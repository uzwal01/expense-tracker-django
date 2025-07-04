 
# Django Expense Tracker API

## Overview
A REST API for personal expense and income tracking with JWT authentication.  
Supports multiple users, permission control, tax calculation, and pagination.

---

## Features
- User registration and login with JWT tokens  
- Create, Read, Update, Delete expense/income records  
- Automatic tax calculations (flat and percentage)  
- Regular users manage only their own data; superusers manage all records  
- Paginated list responses for performance  

---

## Technologies
- Python 3.8+  
- Django 4.x  
- Django REST Framework  
- djangorestframework-simplejwt  
- SQLite (default database)  

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/uzwal01/expense-tracker-django
cd expense_tracker

```

### 2. Create and activate virtual environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate

```

### 5. Create Superuser(optional)

```bash
python manage.py createsuperuser

```

### 6. Start the server

```bash
python manage.py runserver

```

## API Endpoints


| Method | Endpoint              | Description          | Request Body                         | Response                          |
| ------ | --------------------- | -------------------- | ------------------------------------ | --------------------------------- |
| POST   | `/api/auth/register/` | Register new user    | `{ "username": "", "password": "" }` | `{ "message": "User created" }`   |
| POST   | `/api/auth/login/`    | Login user (get JWT) | `{ "username": "", "password": "" }` | `{ "access": "", "refresh": "" }` |
| POST   | `/api/auth/refresh/`  | Refresh JWT token    | `{ "refresh": "" }`                  | `{ "access": "" }`                |


## Expenses and Income

| Method | Endpoint              | Description           | Request Body (POST/PUT)                                   | Response                              |                 |                        |
| ------ | --------------------- | --------------------- | --------------------------------------------------------- | ------------------------------------- | --------------- | ---------------------- |
| GET    | `/api/expenses/`      | List user's records   | -                                                         | Paginated list of records             |                 |                        |
| POST   | `/api/expenses/`      | Create new record     | \`{ "title": "", "amount": 0, "transaction\_type": "debit | credit", "tax": 0, "tax\_type": "flat | percentage" }\` | Created record details |
| GET    | `/api/expenses/{id}/` | Get a specific record | -                                                         | Single record details                 |                 |                        |
| PUT    | `/api/expenses/{id}/` | Update a record       | Same as POST body                                         | Updated record details                |                 |                        |
| DELETE | `/api/expenses/{id}/` | Delete a record       | -                                                         | 204 No Content                        |                 |                        |


---

## Testing

Use Postman or similar tool for API testing:

- Register and login to get JWT tokens

- Use Bearer token in Authorization header for protected endpoints

- Test CRUD and permission edge cases as explained in the walkthrough

