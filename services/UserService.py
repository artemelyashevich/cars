from flask import Response
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
        user = self.userDAO.get_by_id(id)
        if self.validate.check_user(user):
            try:
                return self.convert.convert_data_user(user)
            except Exception as err:
                print(err)
                return Response(status=500)
        return Response(status=400)

    def create(self, data: dict) -> dict | Response:
        if self.validate.check_data(data):
            try:
                user = User(name=data.get('name'), email=data.get('email'))
                return self.convert.convert_data_user(self.userDAO.create(user))
            except Exception as err:
                print(err)
                return Response(status=500)
        return Response(status=400)

    def update(self, id: int, _data: dict) -> User | Response:
        user = self.userDAO.get_by_id(id)
        try:
            if self.validate.check_user(user):
                data = self.validate.update_data(_data, user)
                return self.convert.convert_data_user(self.userDAO.update(id, data))
        except Exception as err:
            print(err)
            return Response(status=500)
        return Response(status=400)

    def delete(self, id: int) -> Response:
        user = self.userDAO.get_by_id(id)
        if self.validate.check_user(user):
            try:
                self.userDAO.delete(user)
                return Response(status=204)
            except Exception as err:
                print(err)
                return Response(status=500)
        return Response(status=404)
