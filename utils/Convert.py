from flask import jsonify

from models.Car import Car
from models.User import User


class Convert:

    def convert_data_user(self, user: User) -> dict:
        return jsonify({
            "id": user.get_id(),
            "name": user.get_name(),
            "email": user.get_email(),
            "balance": user.get_balance(),
            "age": user.get_age(),
            "photo": user.get_photo(),
            "is_Admin": user.get_is_admin(),
            "is_Employee": user.get_is_employee(),
            "create_date": user.get_create_date(),
            "login_date": user.get_login_date(),
        })

    def convert_data_car(self, car: Car) -> dict:
        return jsonify({
            "id": car.get_id(),
            "title": car.get_title(),
            "description": car.get_description(),
            "price": car.get_price(),
            "model": car.get_model(),
            "type": car.get_type(),
            "photo": car.get_photo(),
            "is_published": car.get_is_published(),
            "employee_id": car.get_employee_id(),
            "create_date": car.get_create_date(),
        })
