from flask import Blueprint, request
from services.UserService import UserService

user_route = Blueprint('user', __name__)

userService = UserService()


@user_route.route('/<id>', methods=['GET'])
def get_user(id: int):
    return userService.get(id)


@user_route.route('/', methods=["GET"])
def get_all():
    return userService.get_all()


@user_route.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    return userService.create(data)


@user_route.route('/', methods=['PUT'])
def update_user():
    data = request.get_json()
    return userService.update(data)


@user_route.route('/', methods=['DELETE'])
def delete_user():
    return userService.delete()


@user_route.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    return userService.login(data)


@user_route.route('/logout', methods=['POST'])
def logout_user():
    return userService.logout()
