from flask import Blueprint, request
from services.UserService import UserService

user_route = Blueprint('user', __name__)

userService = UserService()


@user_route.route('/<id>', methods=['GET'])
def get_user(id: int):
    return userService.get(id)


@user_route.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    return userService.create(data)


@user_route.route('/<id>', methods=['PUT'])
def update_user(id: int):
    data = request.get_json()
    return userService.update(id, data)


@user_route.route('/<id>', methods=['DELETE'])
def delete_user(id: int):
    return userService.delete(id)
