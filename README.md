# vehicle-management-api
A RESTful API for managing vehicles, calculating insurance premiums based on vehicle type and cost. Built with **FastAPI**, **SQLAlchemy**, and **Pydantic**, using **SQLite** as the backend database.

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

