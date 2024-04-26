from flask import Blueprint, jsonify, request
from models.user import User
from database.db import db

user_controller = Blueprint('user', __name__)


@user_controller.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name} for user in users]), 200


@user_controller.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return jsonify(
            {"id": user.id, "name": user.name, "phone_number": user.phone_number, "company_id": user.company_id}), 200
    return jsonify({"message": "User not found"}), 404


@user_controller.route('/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.phone_number = data.get('phone_number', user.phone_number)
    db.session.commit()
    return jsonify({"message": "User updated successfully."}), 200


@user_controller.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully."}), 200
