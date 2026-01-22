from flask import request, jsonify
from app.services.todo_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task
)

def create_task_controller():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    task = create_task(data)
    return jsonify(task_to_dict(task)), 201


def get_tasks_controller():
    tasks = get_all_tasks()
    return jsonify([task_to_dict(t) for t in tasks]), 200


def get_task_controller(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task_to_dict(task)), 200


def update_task_controller(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task = update_task(task, data)
    return jsonify(task_to_dict(task)), 200


def delete_task_controller(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    delete_task(task)
    return jsonify({"message": "Task deleted successfully"}), 200


def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "is_completed": task.is_completed,
        "created_at": task.created_at
    }
