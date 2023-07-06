from datetime import datetime
from db.connection import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name: str = db.Column(db.VARCHAR(255), nullable=False)
    email: str = db.Column(db.VARCHAR(255), nullable=False)
    balance: float = db.Column(db.Float)
    age: int = db.Column(db.Integer)
    photo: str = db.Column(db.VARCHAR(255))
    is_admin: bool = db.Column(db.Boolean, default=False)
    is_employee: bool = db.Column(db.Boolean, default=False)
    create_date: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, balance, age, photo):
        self.name = name
        self.email = email
        self.balance = balance
        self.age = age
        self.photo = photo

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_balance(self) -> float:
        return self.balance

    def get_address(self) -> str:
        return self.address

    def get_age(self) -> int:
        return self.age

    def get_photo(self) -> str:
        return self.photo

    def get_is_admin(self) -> bool:
        return self.is_admin

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Balance: {self.balance}\n" \
               f"Address: {self.address}\n" \
               f"Age: {self.age}\n" \
               f"Photo: {self.photo}\n" \
               f"is_admin: {self.is_admin}\n" \
               f"Create_date: {self.create_date}\n"

