from flask import Blueprint
from app.controllers.todo_controller import (
    create_task_controller,
    get_tasks_controller,
    get_task_controller,
    update_task_controller,
    delete_task_controller
)

api_bp = Blueprint("api", __name__)

api_bp.route("/tasks", methods=["POST"])(create_task_controller)
api_bp.route("/tasks", methods=["GET"])(get_tasks_controller)
api_bp.route("/tasks/<int:task_id>", methods=["GET"])(get_task_controller)
api_bp.route("/tasks/<int:task_id>", methods=["PUT"])(update_task_controller)
api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])(delete_task_controller)

