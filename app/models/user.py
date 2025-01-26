from sqlalchemy import Column, String, UUID
import uuid
from app.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        unique=True,
        nullable=False,
        default=uuid.uuid4,
    )
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    patronymic = Column(String, nullable=True)
    email = Column(String, unique=True, index=True)
