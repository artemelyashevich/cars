from dao.MixinDAO import MixinDao
from models.User import User


class UserDao(MixinDao):

    def get_by_email(self, _email: str) -> User:
        return self.db.session.query(User).filter_by(email=_email).first()

    def update(self, _id: int, data: dict) -> User:
        user = self.get_by_id(_id, User)
        print(user)
        user.name = str(data.get('name'))
        user.email = str(data.get('email'))
        user.photo = str(data.get('photo'))
        user.age = int(data.get('age'))
        user.is_employee = bool(data.get('is_employee'))
        user.is_admin = bool(data.get('is_admin'))
        user.balance = float(data.get('balance'))
        self.db.session.commit()

        return user
