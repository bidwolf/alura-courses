import os

from dotenv import load_dotenv

load_dotenv()  # This line read .env configuration
SECRET_KEY = os.getenv("APP_SECRET_KEY")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")
SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads"
