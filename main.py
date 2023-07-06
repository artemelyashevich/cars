import os
from dotenv import load_dotenv
from flask import Flask
from routes.carPoutes import car_route
from routes.userRoutes import user_route

app = Flask(__name__)

load_dotenv()
app.config[
    "SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://root:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/{os.getenv("NAME")}'
from db.connection import db
db.init_app(app)
from models import User, Car
app.register_blueprint(user_route, url_prefix='/api/v1/user')
app.register_blueprint(car_route, url_prefix='/api/v1/car')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=9000)
