from datetime import datetime
from db.connection import db


class Car(db.Model):
    __tablename__ = 'car'
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title: str = db.Column(db.VARCHAR(255), nullable=False)
    description: str = db.Column(db.Text, nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    model: str = db.Column(db.VARCHAR(255), nullable=False)
    type: str = db.Column(db.VARCHAR(30), nullable=False)
    photo: str = db.Column(db.VARCHAR(255))
    is_published: bool = db.Column(db.Boolean, default=False)
    employee_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))
    create_date: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description, price, model, type, employee_id):
        self.title = title
        self.description = description
        self.price = price
        self.model = model
        self.type = type
        self.employee_id = employee_id

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_model(self):
        return self.model

    def get_type(self):
        return self.type

    def get_photo(self):
        return self.photo

    def get_employee_id(self):
        return self.employee_id

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Description: {self.description}\n" \
               f"Price: {self.price}\n" \
               f"Model: {self.model}\n" \
               f"Type: {self.type}\n" \
               f"Employee_id: {self.employee_id}\n" \
               f"Create_date: {self.create_date}\n"

