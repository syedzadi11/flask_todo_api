from app.schemas.todo_schema import TaskSchema
from marshmallow import ValidationError
from flask import request, jsonify
from app.services.todo_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task
)

task_schema = TaskSchema()


def create_task_controller():
    try:
        schema = TaskSchema()
        data = schema.load(request.get_json())  

        task = create_task(data)
        return jsonify(task.to_dict()), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400





def get_tasks_controller():
    tasks = get_all_tasks()
    return jsonify([t.to_dict() for t in tasks]), 200



def get_task_controller(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify([t.to_dict() for t in task]), 200



def update_task_controller(task_id):
    try:
        task = get_task_by_id(task_id)
        if not task:
            return jsonify({"error": "Task not found"}), 404

        data = TaskSchema(partial=True).load(request.get_json())
        task = update_task(task, data)

        return jsonify(task.to_dict()), 200

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    except Exception as e:
        return jsonify({"error": "Something went wrong"}), 500




def delete_task_controller(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    delete_task(task)
    return jsonify({"message": "Task deleted successfully"}), 200



