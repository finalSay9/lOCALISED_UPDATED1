from pydantic import BaseModel


class Base(BaseModel):
    username: str
    displayname: str
    


class CreateUser(Base):
    password: str


class UserResponse(Base):
    id: int