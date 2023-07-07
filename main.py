from dotenv import load_dotenv
from flask import Flask
from db.config import ApplicationConfig
from routes.carRoutes import car_route
from routes.userRoutes import user_route

app = Flask(__name__)

load_dotenv()
app.config.from_object(ApplicationConfig)

from db.connection import db

db.init_app(app)
from models import User
from models import Car

app.register_blueprint(user_route, url_prefix='/api/v1/user')
app.register_blueprint(car_route, url_prefix='/api/v1/car')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=9000)
