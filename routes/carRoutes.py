from flask import Blueprint, request
from services.CarService import CarService

car_route = Blueprint('car', __name__)

carService = CarService()


@car_route.route('/', methods=["POST"])
def create() -> dict:
    data = request.get_json()
    return carService.create(data)


@car_route.route('/<int:id>', methods=["GET"])
def get(id: int) -> dict:
    return carService.get(id)


@car_route.route('/<int:id>', methods=["DELETE"])
def delete(id: int):
    return carService.delete(id)


@car_route.route('/<int:id>', methods=["PUT"])
def update(id: int):
    data = request.get_json()
    return carService.update(id, data)
