# Internship Task: Expense Tracker API

This project is a Django REST API for tracking expenses and incomes, featuring JWT authentication, CRUD operations, and tax calculations. It is designed as a learning project for backend development with Django and Django REST Framework.

## Features
- Django Project Setup
- JWT Authentication (Register/Login/Refresh)
- ExpenseIncome Model
- CRUD API with ViewSet
- Permissions (Owner or Admin only)
- Total calculation (Flat & Percentage tax)
- Pagination (page & page_size supported)

## Project Structure
```
expenseapi/         # Django project settings and URLs
tracker/            # App containing models, views, serializers, permissions, viewsets
  ├── models.py     # ExpenseIncome model
  ├── views.py      # Register and ExpenseIncome API views
  ├── serializers/  # Serializers for API
  ├── permissions/  # Custom permissions
  ├── viewsets/     # ViewSets for API
  └── migrations/   # Database migrations
```

## Requirements
- Python 3.8+
- Django 5.x
- djangorestframework
- djangorestframework-simplejwt

Install dependencies:
```bash
 pip install django djangorestframework 
 pip install djangodjangorestframework-simplejwt

## Setup & Run
1. **Clone the repository**
2. **Install dependencies** (see above)
3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/register/` — Register a new user
- `POST /api/auth/login/` — Obtain JWT token (username, password)
- `POST /api/auth/refresh/` — Refresh JWT token

### Expense/Income
- `GET /api/expenses/` — List all records (paginated)
- `POST /api/expenses/` — Create a new record
- `GET /api/expenses/{id}/` — Retrieve a record
- `PUT /api/expenses/{id}/` — Update a record
- `DELETE /api/expenses/{id}/` — Delete a record

#### Example ExpenseIncome Model
```json
{
  "user": 1,
  "title": "Salary",
  "description": "Monthly salary",
  "amount": 1000.00,
  "transaction_type": "credit", // or "debit"
  "tax": 10.00,
  "tax_type": "flat" // or "percentage"
}
```
- **total**: Calculated as `amount + tax` (flat) or `amount + (amount * tax / 100)` (percentage)

### Permissions
- Only the owner or admin can access/modify their records.

### Pagination
- Supports `?page=` and `?page_size=` query params.

## Development
- To run tests (if implemented):
   python manage.py test
  - To create a superuser for admin access:
  python manage.py createsuperuser
  

## Notes
- The database used is SQLite by default (`db.sqlite3`).
- Environment variables and sensitive files should be kept out of version control (see `.gitignore`).

## GitHub Upload Steps
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <https://github.com/boharapashupati/intership-task.git>
git push -u origin main
