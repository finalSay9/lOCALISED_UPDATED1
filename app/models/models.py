from sqlalchemy import (
    Column, String, Boolean, DateTime, ForeignKey,
    Text, Enum as SAEnum, Integer, Table
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum


from app.core.database import Base



# ─── Enums ────────────────────────────────────────────────────────────────────

class UserStatus(str, enum.Enum):
    online = "online"
    away = "away"
    offline = "offline"


class RoomType(str, enum.Enum):
    channel = "channel"
    dm = "dm"


class MessageStatus(str, enum.Enum):
    sent = "sent"
    delivered = "delivered"
    read = "read"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    display_name = Column(String(100), nullable=False)
    hashed_password = Column(String, nullable=False)
    status = Column(SAEnum(UserStatus), default=UserStatus.offline)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())