from fastapi import APIRouter, Depends
from app.database import users_collection
from app.utils import get_current_user

router = APIRouter()

@router.get("/users")
async def get_all_users(token: str = Depends(get_current_user)):
    users = await users_collection.find().to_list(100)
    return users
