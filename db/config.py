import os
from dotenv import load_dotenv

load_dotenv()


class ApplicationConfig:
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/{os.getenv("NAME")}'

    SESSION_TYPE = os.getenv("SESSION_TYPE")
    SESSION_PERMANENT = os.getenv("SESSION_PERMANENT")
    SESSION_USE_SINGER = os.getenv("SESSION_USE_SINGER")
