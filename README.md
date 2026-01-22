# Single-User To-Do API

This is a simple **Todo REST API** built using **Flask**, **Flask-SQLAlchemy**, and **Flask-Migrate**.  
The API allows users to create, update, and manage todo tasks.

---

##  Features

- Create a new task
- Update task status (completed / not completed)
- RESTful API structure
- MySQL database integration
- Flask Blueprints used
- Flask-Migrate for database migrations

---

##  Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- MySQL
- PyMySQL
- Postman (for API testing)

---

## 📂 Project Structure

todo_api/
│
├── app/
│ ├── init.py
│ ├── extensions.py
│ ├── models.py
│ └── api/
│ ├── init.py
│ └── routes.py
│
├── migrations/
├── venv/
├── run.py
├── requirements.txt
├── .gitignore
└── README.md

## API Endpoints

### Create Task

**POST /tasks**  
Request Body (JSON):
```json
{
  "title": "Learn Flask",
  "description": "Build Todo API"
}

Response:

Json
{
  "id": 1,
  "title": "Learn Flask",
  "description": "Build Todo API",
  "is_completed": false,
  "created_at": "2026-01-15T15:00:00"
}

 ### Get All Tasks

 **GET /tasks**
Response: List of all tasks in JSON

Get Single Task 

GET /tasks
Response: JSON of a single task

Update Task

PUT /tasks
Request Body (JSON):

Json
{
  "title": "Learn Flask - Updated",
  "description": "Update the task",
  "is_completed": true
}
Response: Updated task JSON


Delete Task

DELETE /tasks
Response: Success message 

**Setup / How to Run**
**Create MySQL database

Sql
CREATE DATABASE todo_db;
Set DATABASE_URL in .env


DATABASE_URL=mysql+pymysql://root:@localhost/todo_db
Install requirements

Bash
pip install -r requirements.txt
Run database migrations


Bash
flask db upgrade
Start the Flask server  


Bash
python run.py



**Notes**
Make sure MySQL server is running (via XAMPP).
Use Postman or any API client to test the endpoints.
All date/time fields are in UTC format.