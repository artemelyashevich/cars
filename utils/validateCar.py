from models.Car import Car


class Validate:

    @staticmethod
    def check_data(data: dict) -> bool:
        if data.get('title') is None \
                or data.get('employee_id') is None \
                or data.get('description') is None \
                or data.get('price') is None \
                or data.get('model') is None \
                or data.get('type') is None:
            return False
        return True

    @staticmethod
    def check_car(car: Car | None) -> bool:
        return car is not None

    @staticmethod
    def update_car(data: dict, car: Car) -> dict:
        if data.get('title') is None:
            data['title'] = car.get_title()
        if data.get('description') is None:
            data['description'] = car.get_description()
        if data.get('employee_id') is None:
            data['employee_id'] = car.get_employee_id()
        if data.get('price') is None:
            data['price'] = car.get_price()
        if data.get('model') is None:
            data['model'] = car.get_model()
        if data.get('type') is None:
            data['type'] = car.get_type()
        if data.get('photo') is None:
            data['photo'] = car.get_photo()
        return data
