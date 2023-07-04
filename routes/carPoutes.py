from flask import Blueprint

car_route = Blueprint('car', __name__)

@car_route.route('/car')
def index():
    return "This is an example car"