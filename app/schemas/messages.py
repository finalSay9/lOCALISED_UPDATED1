from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime
# from models import UserStatus, RoomType, MessageStatus


class Base(BaseModel):
    username: str
    displayname: str
    status: UserStatus
    created_at: datetime

    model_config = {"from_attributes": True}

    


class CreateUser(Base):
    password: str


class UserResponse(Base):
    id: int