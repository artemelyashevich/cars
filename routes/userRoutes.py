from flask import Blueprint
from services.UserService import UserService

user_route = Blueprint('user', __name__)

@user_route.route('/')
def index():
    return "Hello"