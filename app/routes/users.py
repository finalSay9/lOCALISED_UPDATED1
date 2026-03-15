from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.models import User
from app.schemas import schemas
from app.security.authenticate import hash_password


router = APIRouter(prefix="/users", tags=["users"])


@router.post('/register', response_model=schemas.CreateUser)
async def register(user: schemas.CreateUser, db: AsyncSession = Depends(get_db)):
    #checking if the user already exist
    existing_user = await db.execute(
        select(User).where(User.username == user.username) 

      ).scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    user_db = User(
        username=user.username,
        display_name=user.display_name,
        hashed_password=hash_password(user.password),
    )
    await db.add(user)
    await db.commit()
    await db.refresh(user)

    return user_db