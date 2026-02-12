from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from app.extensions import db, bcrypt
from app.models.user import User

auth_bp = Blueprint("auth", __name__)

#---------------Register---------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400

    # check user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"msg": "username already exists"}), 400

    # hash password
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(
        username=username,
        password_hash=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


# ---------------- LOGIN ----------------
@auth_bp.route("/login", methods=["POST"])  
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"msg": "Invalid username or password"}), 401

    # password check
    if not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"msg": "Invalid username or password"}), 401

    # JWT token generate
    access_token = create_access_token(identity=user.id)

    return jsonify({"token": access_token}), 200