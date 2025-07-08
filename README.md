# 🐞 Bug Tracker Web App

A simple and user-friendly bug tracking system built with **Flask**, **SQLite**, and **Bootstrap**.  
Log, edit, resolve, and delete bugs with a responsive web interface and automated testing via PyTest.

---

## 🚀 Features

- Add and manage bugs
- Mark bugs as resolved
- Edit or delete bugs
- Responsive UI (Bootstrap)
- Fully tested with PyTest

---

## 🛠️ Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the Database

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### 4. Run the App

```bash
flask run
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ✅ Running Tests

```bash
pytest
```

Tests cover all CRUD operations: Add, Edit, Delete, Resolve.

---

## 📁 Project Structure

```
bug-tracker/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   │   ├── index.html
│   │   └── edit.html
│   └── static/
│       └── style.css
│
├── tests/
│   ├── conftest.py
│   └── test_app.py

├── instance/
│   └── bugs.db
│
├── config.py
├── run.py
├── README.md
├── README.txt
├── requirements.txt
└── .gitignore
```

---

## 🧪 Manual Testing Checklist

- Home page loads with form and table
- Bug can be added, edited, resolved, and deleted
- Input validation and UI response works

---

## 📜 License

MIT License