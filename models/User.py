class User:

    def __init__(self, name, email, balance, address, age, photo):
        self.name = name
        self.email = email
        self.balance = balance
        self.address = address
        self.age = age
        self.photo = photo
        self.is_admin = False

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
               f"is_admin: {self.is_admin}\n"
