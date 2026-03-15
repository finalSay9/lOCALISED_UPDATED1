from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime

from app.models.models import UserStatus
# from models import UserStatus, RoomType, MessageStatus


class Base(BaseModel):
    username: str
    displayname: str
    


class CreateUser(Base):
    password: str


class UserResponse(Base):
    id: int
    status: UserStatus
    created_at: datetime

    model_config = {"from_attributes": True}