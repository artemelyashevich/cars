from flask import Response, session

from dao.CarDAO import CarDao
from models.Car import Car
from utils.Convert import Convert
from utils.validateCar import Validate


class CarService:
    def __init__(self):
        self.carDAO = CarDao()
        self.convert = Convert()
        self.validate = Validate()

    def get(self, id: int) -> dict | Response:
        car = self.carDAO.get_by_id(id, Car)
        if self.validate.check_car(car):
            try:
                return self.convert.convert_data_car(car)
            except Exception as e:
                print(e)
                return Response(status=500)
        return Response(status=400)

    def get_all(self) -> list | Response:
        data = []
        for car in self.carDAO:
            data.append(self.convert.convert_data_car(car))
        return data

    def create(self, data: dict) -> dict | Response:
        user_id = session.get('user_id')
        if user_id and self.validate.check_data(data):
            try:
                car = Car(title=data.get('title'), description=data.get('description'),
                          price=data.get('price'), model=data.get('model'), type=data.get('type'),
                          employee_id=user_id)
                return self.convert.convert_data_car(self.carDAO.create(car))
            except Exception as e:
                print(e)
                return Response(status=500)
        return Response(status=401)

    def update(self, id: int, data: dict) -> dict | Response:
        user_id = session.get('user_id')
        if user_id:
            print(id)
            car = self.carDAO.get_by_id(id, Car)
            try:
                if self.validate.check_car(car):
                    data = self.validate.update_car(data, car)
            except Exception as e:
                print(e)
                return Response(status=500)
        return self.convert.convert_data_car(self.carDAO.update(id, data))

    def delete(self, id: int) -> Response:
        car = self.carDAO.get_by_id(id, Car)
        if session.get("user_id") == car.get_employee_id():
            try:
                car = self.carDAO.get_by_id(id, Car)
                self.carDAO.delete(car)
                return Response(status=204)
            except Exception as e:
                print(e)
                return Response(status=500)
        return Response(status=401)

    def search_car(self, q: str) -> list:
        cars = self.carDAO.get_by_title(q)
        data = []
        for car in cars:
            data.append(self.convert.convert_data_car(car))
        return data
