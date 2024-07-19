from typing import List

from fastapi import APIRouter, HTTPException

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService(UserRepository())

@router.post("/users/", response_model=User)
def create_user(user: User):
    return user_service.create_user(user)
@router.post("/users/batch", response_model=List[User])
def create_users(users: List[User]):
    return user_service.create_users(users)

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=List[User])
def list_users():
    return user_service.list_users()
