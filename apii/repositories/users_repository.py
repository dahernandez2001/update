from models.db import db
from models.users_model import User

class UsersRepository:
    def create_user(self, data):
        new_user = User(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            role=data.get('role', 'user')
        )
        db.session.add(new_user)
        db.session.commit()
        return {"message": "Usuario registrado exitosamente"}

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()
