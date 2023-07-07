from db.connection import db


class MixinDao:

    def __init__(self):
        self.db = db

    def get_by_id(self, _id: int, model):
        return self.db.session.query(model).get(_id)

    def get_all(self, model) -> list:
        return self.db.session.query(model).all()

    def create(self, item):
        self.db.session.add(item)
        self.db.session.commit()
        return item

    def delete(self, item):
        self.db.session.delete(item)
        self.db.session.commit()
