# 🚗 Vehicle Management API

A RESTful API built with **FastAPI + SQLAlchemy** for managing vehicles. Supports creating, reading, updating, and deleting vehicle records.

---
## ✅ Features

- Create a vehicle record with cost and type
- Automatically calculate insurance premium
- Read vehicle details
- Update vehicle cost/type and auto-recalculate premium
- Delete vehicle records
- API documentation via Swagger UI

---

## 🚀 Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Framework   | FastAPI           |
| ORM         | SQLAlchemy        |
| Validation  | Pydantic          |
| Database    | SQLite (dev)      |
| API Docs    | Swagger / Redoc   |

---

## 🧠 Premium Calculation Logic

| Vehicle Type   | Premium Rate |
|----------------|--------------|
| Two Wheeler    | 2% of cost   |
| Four Wheeler   | 6% of cost   |

---

## Project Structure
```bash
vehicle_app/
├── main.py             # FastAPI app
├── models.py           # SQLAlchemy DB models
├── schemas.py          # Pydantic models
├── database.py         # DB session and setup
└── crud.py             # DB logic (create, read, update)
```
---

## 📦 Installation

1. **Clone the repository**
   
```bash
git clone https://github.com/wtavi00/vehicle-management-api.git
cd vehicle-management-api
```

2.**Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3.**Install dependencies**
```bash
git clone https://github.com/wtavi00/vehicle-management-api.git
cd vehicle-management-api
pip install -r requirements.txt
```


##  Example API Usage

### POST /vehicles/
{
  "vehicle_id": "V1001",
  "vehicle_type": "Four Wheeler",
  "cost": 1000000
}

### PUT /vehicles/V1001
{
  "vehicle_type": "Two Wheeler",
  "cost": 200000
}

### DELETE /vehicles/V1001
-No body required.

## Environment Configuration
For production, consider switching to PostgreSQL:
# database.py
DATABASE_URL = "postgresql://username:password@localhost:5432/yourdb"

## ✨ Author
[Avijit Tarafder](https://github.com/wtavi00)

## 📜 License
[MIT License](https://github.com/wtavi00/vehicle-management-api/blob/main/LICENSE)
