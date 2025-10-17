from flask import Blueprint, request, jsonify
from services.users_services import UserService

user_bp = Blueprint('user_bp', __name__)
user_service = UserService()

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = user_service.register_user(data)
    return jsonify(result), result.get('status', 200)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = user_service.login_user(data)
    return jsonify(result), result.get('status', 200)
