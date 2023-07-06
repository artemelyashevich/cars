from datetime import datetime
from db.connection import db


class Car(db.Model):
    __tablename__ = 'car'
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title: str = db.Column(db.VARCHAR(255), nullable=False)
    description: str = db.Column(db.Text, nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    model: str = db.Column(db.VARCHAR(255), nullable=False)
    type: str = db.Column(db.VARCHAR(30), nullable=False)
    photo: str = db.Column(db.VARCHAR(255))
    is_published: bool = db.Column(db.Boolean, default=False)
    employee_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))
    create_date: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title: str, description: str, price: float, model: str, type: str, employee_id: int):
        self.title = title
        self.description = description
        self.price = price
        self.model = model
        self.type = type
        self.employee_id = employee_id

    def get_id(self) -> int:
        return id

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def get_model(self) -> str:
        return self.model

    def get_type(self) -> str:
        return self.type

    def get_photo(self) -> str:
        return self.photo

    def get_employee_id(self) -> int:
        return self.employee_id

    def get_is_published(self) -> bool:
        return self.is_published

    def get_create_date(self) -> datetime:
        return self.create_date

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Description: {self.description}\n" \
               f"Price: {self.price}\n" \
               f"Model: {self.model}\n" \
               f"Type: {self.type}\n" \
               f"Employee_id: {self.employee_id}\n" \
               f"Create_date: {self.create_date}\n"
