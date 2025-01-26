from pydantic import BaseModel, EmailStr, UUID4


class CreateUser(BaseModel):
    name: str
    surname: str
    patronymic: str | None = None
    email: EmailStr

    class Config:
        from_attributes = True


class UserResponse(CreateUser):
    id: UUID4
