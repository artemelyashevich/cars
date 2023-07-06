from datetime import datetime
from db.connection import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.VARCHAR(255), nullable=False)
    email: str = db.Column(db.VARCHAR(255), nullable=False)
    balance: float = db.Column(db.Float, default=0)
    age: int = db.Column(db.Integer, default=0)
    photo: str = db.Column(db.VARCHAR(255))
    is_admin: bool = db.Column(db.Boolean, default=False)
    is_employee: bool = db.Column(db.Boolean, default=False)
    last_login: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    create_date: datetime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_balance(self) -> float:
        return self.balance

    def get_age(self) -> int:
        return self.age

    def get_photo(self) -> str:
        return self.photo

    def get_is_admin(self) -> bool:
        return self.is_admin

    def get_is_employee(self) -> bool:
        return self.is_employee

    def get_create_date(self) -> datetime:
        return self.create_date

    def get_login_date(self) -> datetime:
        return self.last_login

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Balance: {self.balance}\n" \
               f"Age: {self.age}\n" \
               f"Photo: {self.photo}\n" \
               f"is_admin: {self.is_admin}\n" \
               f"is_employee: {self.is_employee}\n" \
               f"Create_date: {self.create_date}\n"
