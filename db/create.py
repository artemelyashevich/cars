import os
from dotenv import load_dotenv

import pymysql

load_dotenv()


def create():
    try:
        connection = pymysql.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            user=os.getenv("NAME"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Database connected...")
        try:

            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `user`" \
                                     "(id int AUTO_INCREMENT, " \
                                     "name varchar(255), " \
                                     "password varchar(255), " \
                                     "balance int, " \
                                     "photo text, " \
                                     "age int, " \
                                     "is_admin bool, " \
                                     "address varchar(255), " \
                                     "email varchar(255), PRIMARY KEY (id));"
                cursor.execute(create_table_query)
                print("Table created!")

        finally:
            connection.close()
            print('Close connection')
    except Exception as ex:
        print(ex)
