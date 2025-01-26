from app.db.base import get_session
from app.dtos.user_dtos import CreateUser, UserResponse
from app.models.user import User
from fastapi import Body, Depends
from sqlalchemy.orm import Session


def create(
    user: CreateUser = Body(..., title="Dto для создания нового пользователя."),
    db: Session = Depends(get_session),
) -> UserResponse:
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
