# 🏥 Patient Management System API

A RESTful **Patient Management System API** built with **FastAPI**, **SQLAlchemy**, **MySQL**, and **Alembic**. Implements complete CRUD (Create, Read, Update, Delete) operations for managing **Patients**.

---

## 🚀 Features

- Patient Management (CRUD)
- Request & Response Validation using Pydantic
- MySQL Database Integration
- SQLAlchemy ORM
- Database Versioning with Alembic
- Environment Variable Configuration
- Modular Project Structure
- Interactive API Documentation with Swagger UI

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Alembic
- Pydantic
- Uvicorn
- Python Dotenv

---

## 📁 Project Structure

```
patient_management/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   └── patient.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── crud/
│   │   └── patient.py
│   │
│   ├── models/
│   │   └── patient.py
│   │
│   ├── schemas/
│   │   └── patient.py
│   │
│   └── __init__.py
│
├── .env.example
├── .gitignore
├── alembic.ini
├── main.py
├── Readme.md
└── requirements.txt
```

---

## 🗄️ Database Model

### Patient

- ID
- Name
- Age
- Gender
- Phone

---

## 📌 API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/patients/`      | Create Patient    |
| GET    | `/patients/`      | Get All Patients  |
| GET    | `/patients/{id}` | Get Patient by ID |
| PUT    | `/patients/{id}` | Update Patient    |
| DELETE | `/patients/{id}` | Delete Patient    |

---

## ⚙️ Installation

### Clone the Repository

```
git clone <your-repo-url>
cd patient_management
```

### Create Virtual Environment

```
python -m venv patient_env
```

### Activate Virtual Environment

**Windows**

```
patient_env\Scripts\activate
```

**Linux / macOS**

```
source patient_env/bin/activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=patient_db
```

---

## 🔄 Database Migration

Generate Migration

```
alembic revision --autogenerate -m "Initial Migration"
```

Apply Migration

```
alembic upgrade head
```

---

## ▶️ Running the Application

```
uvicorn main:app --reload
```

Application URL: `http://127.0.0.1:8000`

---

## 📖 API Documentation

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## 🏗️ Project Architecture

- **Models** → Database tables using SQLAlchemy
- **Schemas** → Request and response validation using Pydantic
- **CRUD** → Database operations and business logic
- **API** → REST endpoints and routing
- **Core** → Database connection and configuration
- **Alembic** → Database migration management

---

## 📜 License

This project is created for learning and educational purposes (SMIT Agentic AI course assignment).
