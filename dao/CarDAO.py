from dao.MixinDAO import MixinDao
from models.Car import Car


class CarDao(MixinDao):

    def get_by_model(self, model: str) -> list | object:
        return self.db.session.query(Car).filter_by(model=model).all()

    def get_by_price(self, type: str) -> list | object:
        return self.db.session.query(Car).filter_by(type=type).all()

    def get_published(self, is_published: bool) -> list | object:
        return self.db.session.query(Car).filter_by(is_published=is_published).all()

    def get_by_employee(self, id: int) -> list | object:
        return self.db.session.query(Car).filter_by(employee_id=id).all()

    def get_by_title(self, q: str) -> list | object:
        return self.db.session.query(Car).filter(Car.title.like(q)).all()

    def update(self, id, data: dict) -> object:
        car = self.get_by_id(id, Car)
        car.title = data.get('title')
        car.description = data.get('description')
        car.price = data.get('price')
        car.model = data.get('model')
        car.type = data.get('type')
        car.photo = data.get('photo')
        car.is_published = data.get('is_published')
        car.employee_id = data.get('employee_id')

        self.db.session.commit()
        return car
