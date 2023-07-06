from flask import Response
from db.connection import db
from models.User import User


class UserDao:

    def __init__(self):
        self.db = db

    # get methods
    def get_by_id(self, _id: int) -> User:
        return self.db.session.query(User).get(_id)

    def get_by_email(self, _email: str) -> User:
        return self.db.session.query(User).filter_by(email=_email).first()

    def get_all(self) -> list:
        return self.db.session.query(User).all()

    # post methods
    def create(self, user: User) -> User:
        self.db.session.add(user)
        self.db.session.commit()
        return user

    # update methods
    def update(self, _id: int, data: dict) -> User:
        user = self.get_by_id(_id)
        user.name = str(data.get('name'))
        user.email = str(data.get('email'))
        user.photo = str(data.get('photo'))
        user.age = int(data.get('age'))
        self.db.session.commit()

        return user

    # delete methods
    def delete(self, user: User):
        self.db.session.delete(user)
        self.db.session.commit()
