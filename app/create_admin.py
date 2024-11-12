# app/create_admin.py
import asyncio
from app.database import users_collection
from app.utils import hash_password
from app.config import ADMIN_EMAIL, ADMIN_PASSWORD

async def create_admin():
    existing_admin = await users_collection.find_one({"email": ADMIN_EMAIL})
    if not existing_admin:
        admin = {
            "email": ADMIN_EMAIL,
            "password": hash_password(ADMIN_PASSWORD),
            "full_name": "Admin",
            "role": "admin"
        }
        await users_collection.insert_one(admin)
        print("Admin created")
    else:
        print("Admin already exists")

if __name__ == "__main__":
    asyncio.run(create_admin())
