BUG TRACKER WEB APP
-------------------

A simple bug tracking system built using Flask, SQLite, HTML, CSS, and Bootstrap. 
It allows users to log, edit, resolve, and delete bugs. 
The app is fully tested using PyTest and styled with Bootstrap and custom CSS.

-------------------
FEATURES
-------------------

- Add bugs with title, description, and priority
- View all bugs in a table
- Edit and update bug details
- Mark bugs as "Resolved"
- Delete bugs
- Fully responsive and styled interface
- Tested with PyTest for all core functionalities

-------------------
TECHNOLOGIES USED
-------------------

Backend: Flask, SQLAlchemy
Frontend: HTML, CSS, Bootstrap, Jinja2
Database: SQLite
Testing: PyTest
Python version: 3.11+

-------------------
SETUP INSTRUCTIONS
-------------------

1. Clone the repository

   git clone https://github.com/yourusername/bug-tracker.git
   cd bug-tracker

2. Create a virtual environment

   python -m venv venv
   venv\Scripts\activate  (for Windows)
   OR
   source venv/bin/activate  (for Linux/Mac)

3. Install required packages

   pip install flask flask_sqlalchemy pytest or pip install -r requirements.txt

4. Create the database

   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()

5. Run the application

   flask run

   Open your browser at: http://127.0.0.1:5000

-------------------
RUNNING TESTS
-------------------

To run automated tests using PyTest:

   pytest

Tests cover adding, editing, deleting, and resolving bugs.

-------------------
PROJECT STRUCTURE
-------------------

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
│
├── bugs.db
├── config.py
├── run.py
├── README.txt
└── requirements.txt

-------------------
MANUAL TESTING CHECKLIST
-------------------

- Open home page: Should display form and bug table
- Add a bug: Form submission adds the bug to the list
- Edit a bug: Changes appear on the main page
- Mark as resolved: Bug status changes to 'Resolved'
- Delete a bug: Bug is removed from the list

-------------------
CREDITS
-------------------

Developed by Ahmad Sadeed.
Contact: [Add your email or GitHub here if you like]
