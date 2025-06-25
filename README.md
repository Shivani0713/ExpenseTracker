# 💰 Expense Tracker API

A simple Expense Tracker backend built with Django REST Framework (DRF) and JWT Authentication. This project allows users to register, log in, and manage their expenses. Users can create, filter, and analyze their spending by category and date.

---

## 📌 Features

- JWT-based authentication (login & protected endpoints)
- Create, view, and filter expenses
- Category-wise and date-wise analytics
- Simple setup with SQLite (switchable to PostgreSQL/MySQL)
- Clean, RESTful API structure using DRF

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- pip (Python package manager)
- Git (optional)

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/expense-tracker-api.git
cd expense-tracker-api

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
