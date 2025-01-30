import os
from dotenv import load_dotenv

load_dotenv()


class app_config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
