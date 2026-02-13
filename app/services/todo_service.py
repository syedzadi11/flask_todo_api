from app.extensions import db
from app.models.todo import Task

def create_task(data):
    new_task = Task(
        title=data["title"],
        description=data.get("description"),
        user_id=data["user_id"]  
    )
    db.session.add(new_task)
    db.session.commit()
    return new_task



def get_all_tasks(user_id):
    return Task.query.filter_by(user_id=user_id).all()



def get_task_by_id(task_id, user_id):
    return Task.query.filter_by(id=task_id, user_id=user_id).first()



def update_task(task, data):
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.is_completed = data.get("is_completed", task.is_completed)
    db.session.commit()
    return task


def delete_task(task):
    db.session.delete(task)
    db.session.commit()
