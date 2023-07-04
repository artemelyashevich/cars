import os
from dotenv import load_dotenv
from flask import Flask
from flaskext.mysql import MySQL

load_dotenv()
app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_HOST'] = os.getenv("HOST")
app.config['MYSQL_USER'] = os.getenv("USER")
app.config['MYSQL_PASSWORD'] = os.getenv("PASSWORD")
app.config['MYSQL_DB'] = os.getenv("NAME")

mysql.init_app(app)