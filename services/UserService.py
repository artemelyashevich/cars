from datetime import datetime

from flask import Response, session
from werkzeug.security import check_password_hash

from dao.UserDAO import UserDao
from models.User import User
from utils.Convert import Convert
from utils.validateUser import Validate


class UserService:

    def __init__(self):
        self.userDAO = UserDao()
        self.convert = Convert()
        self.validate = Validate()

    def get(self, id: int) -> dict | Response:
        user = self.userDAO.get_by_id(id, User)
        if self.validate.check_user(user):
            try:
                return self.convert.convert_data_user(user)
            except Exception as err:
                print(err)
                return Response(status=500)
        return Response(status=400)

    def get_all(self) -> list:
        data = []
        for user in self.userDAO.get_all(User):
            data.append(self.convert.convert_data_user(user))
        return data

    def create(self, data: dict) -> dict | Response:
        if self.validate.check_data(data):
            try:
                user = User(name=data.get('name'), email=data.get('email'), password=data.get('password'))
                us = self.userDAO.create(user)
                session['user_id'] = us.get_id()
                return self.convert.convert_data_user(us)
            except Exception as err:
                print(err)
                return Response(status=500)
        return Response(status=400)

    def update(self, _data: dict) -> User | Response:
        user_id = session.get('user_id')
        if user_id:
            user = self.userDAO.get_by_id(user_id, User)
            try:
                if self.validate.check_user(user):
                    data = self.validate.update_data(_data, user)
                    return self.convert.convert_data_user(self.userDAO.update(user_id, data))
            except Exception as err:
                print(err)
                return Response(status=500)
            return Response(status=400)
        return Response(status=401)

    def delete(self) -> Response:
        user_id = session.get('user_id')
        if user_id:
            user = self.userDAO.get_by_id(user_id, User)
            if self.validate.check_user(user):
                try:
                    self.userDAO.delete(user)
                    session.pop('user_id')
                    return Response(status=204)
                except Exception as err:
                    print(err)
                    return Response(status=500)
            return Response(status=404)
        return Response(status=401)

    def login(self, data: dict) -> dict | Response:
        email = data.get('email')
        password = data.get('password')
        user = self.userDAO.get_by_email(email)

        if user and check_password_hash(user.password, password):
            user.set_last_login(datetime.utcnow())
            session['user_id'] = user.get_id()
            return self.convert.convert_data_user(user)

        return Response(status=400)

    @staticmethod
    def logout() -> Response:
        session.pop('user_id')
        return Response(status=200)
