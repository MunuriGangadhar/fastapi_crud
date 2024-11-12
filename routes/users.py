from fastapi import APIRouter, HTTPException, Depends
from app.database import users_collection
from app.schemas import UserCreate, UserUpdate, UserResponse
from app.utils import hash_password, decode_access_token, get_current_user
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    user.password = hash_password(user.password)
    new_user = await users_collection.insert_one(user.dict())
    created_user = await users_collection.find_one({"_id": new_user.inserted_id})
    return {"id": str(created_user["_id"]), **created_user}

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, token: str = Depends(get_current_user)):
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": str(user["_id"]), **user}

@router.put("/{user_id}")
async def update_user(user_id: str, user: UserUpdate, token: str = Depends(get_current_user)):
    await users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": user.dict(exclude_unset=True)})
    return {"message": "User updated"}

@router.delete("/{user_id}")
async def delete_user(user_id: str, token: str = Depends(get_current_user)):
    await users_collection.delete_one({"_id": ObjectId(user_id)})
    return {"message": "User deleted"}
