import os

MONGO_URI = os.getenv("MONGO_URI", "your-mongodb-atlas-uri")
DATABASE_NAME = ""
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ADMIN_EMAIL = ""
ADMIN_PASSWORD = ""
