from functools import wraps
from flask import request, jsonify
from config.jwt import verify_token

def role_required(roles):
    if isinstance(roles, str):
        roles = [roles]

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return jsonify({'error': 'Token no proporcionado'}), 401

            token = auth_header.split(" ")[1]
            user_data = verify_token(token)

            if not user_data:
                return jsonify({'error': 'Token inválido o expirado'}), 401

            if user_data.get('role') not in roles:
                return jsonify({'error': 'No autorizado'}), 403

            return f(*args, **kwargs)
        return wrapper
    return decorator
