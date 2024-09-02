import os
from dotenv import load_dotenv

load_dotenv()  # This line read .env configuration
SECRET_KEY = os.getenv("APP_SECRET_KEY")
SQLALCHEMY_DATABASE_URI = "{SGBD}://{user}:{password}@{server}/{database}".format(
    SGBD="mysql+mysqlconnector",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    server=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
)
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads"
