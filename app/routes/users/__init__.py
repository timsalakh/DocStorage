from fastapi import APIRouter, status
from app.dtos.user_dtos import UserResponse
from .create import create as create_user

router = APIRouter(
    prefix="/users",
    tags=["Users section"],
)

router.post("/", response_model=UserResponse, status_code=status.HTTP_200_OK)(
    create_user
)
