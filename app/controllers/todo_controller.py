from flask_jwt_extended import jwt_required, get_jwt_identity
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

@jwt_required()
def create_task_controller():
    try:
        current_user_id = get_jwt_identity()

        schema = TaskSchema()
        data = schema.load(request.get_json())

        
        data["user_id"] = current_user_id

        task = create_task(data)
        return jsonify(task.to_dict()), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400



@jwt_required()
def get_tasks_controller():
    current_user_id = get_jwt_identity()

    tasks = get_all_tasks(current_user_id)

    return jsonify([t.to_dict() for t in tasks]), 200




@jwt_required()
def get_task_controller(task_id):
    current_user_id = get_jwt_identity()

    task = get_task_by_id(task_id, current_user_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    if task.user_id != current_user_id:
        return jsonify({"error": "Forbidden"}), 403

    return jsonify(task.to_dict()), 200




@jwt_required()
def update_task_controller(task_id):
    try:
        current_user_id = get_jwt_identity()

        task = get_task_by_id(task_id,  current_user_id)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        if task.user_id != current_user_id:
            return jsonify({"error": "Forbidden"}), 403

        data = TaskSchema(partial=True).load(request.get_json())
        task = update_task(task, data)

        return jsonify(task.to_dict()), 200

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400





@jwt_required()
def delete_task_controller(task_id):
    current_user_id = get_jwt_identity()

    task = get_task_by_id(task_id, current_user_id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    if task.user_id != current_user_id:
        return jsonify({"error": "Forbidden"}), 403

    delete_task(task)

    return jsonify({"message": "Task deleted successfully"}), 200




