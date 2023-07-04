class UserService:

    def __init__(self, db):
        self.cursor = db.connection.cursor()

    def get_all(self):
        self.cursor.execute(
            "SELECT * FROM `users`"
        )
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
