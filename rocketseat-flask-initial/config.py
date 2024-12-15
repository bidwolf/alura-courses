import os

from dotenv import load_dotenv

load_dotenv()  # This line read .env configuration
SECRET_KEY = os.getenv("APP_SECRET_KEY")
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads"
