from models.User import User


class Validate:

    @staticmethod
    def check_data(data: dict) -> bool:
        if data.get('name') is None or data.get('email') is None or data.get('password') is None:
            return False
        return True

    @staticmethod
    def check_user(user: User | None) -> bool:
        return user is not None

    @staticmethod
    def update_data(data: dict, user: User) -> dict:
        if data.get('user') is None:
            data['user'] = user.get_name()
        if data.get('email') is None:
            data['email'] = user.get_email()
        if data.get('photo') is None:
            data['photo'] = user.get_photo()
        if data.get('age') is None:
            data['age'] = user.get_age()
        return data
