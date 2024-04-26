from flask import Blueprint, request, jsonify
from models.user import User
from database.db import db
import uuid

authentication_controller = Blueprint('authentication', __name__)


@authentication_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(name=data['name']).first()
    if user and user.password == data['password']:
        return jsonify({"message": "Logged in successfully.", "user_id": user.id}), 200
    return jsonify({"message": "Invalid username or password"}), 401


@authentication_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(
        id=str(uuid.uuid4()),
        name=data['name'],
        password=data['password'],
        phone_number=data['phone_number'],
        company_id=data['company_id'],
        is_boss=data['is_boss']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully.", "user_id": new_user.id}), 201
