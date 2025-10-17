import bcrypt
from config.jwt import create_token
from repositories.users_repository import UsersRepository

class UserService:
    def __init__(self):
        self.repo = UsersRepository()

    def register_user(self, data):
        if not data.get('email') or not data.get('password'):
            return {"error": "Email y contraseña requeridos", "status": 400}

        existing = self.repo.get_by_email(data['email'])
        if existing:
            return {"error": "El usuario ya existe", "status": 400}

        hashed_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        data['password'] = hashed_pw.decode('utf-8')
        return self.repo.create_user(data)

    def login_user(self, data):
        user = self.repo.get_by_email(data.get('email'))
        if not user or not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
            return {"error": "Credenciales inválidas", "status": 401}

        token = create_token({'id': user.id, 'email': user.email, 'role': user.role})
        return {"token": token, "role": user.role, "status": 200}
