from db.connection import mysql

class UserDAO:
    def __init__(self):
        self.cursor = mysql.connect().cursor()

    def get_all(self):
        self.cursor.execute(
            "SELECT * FROM `user`"
        )

