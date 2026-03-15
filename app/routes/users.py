from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.models import User
from app.schemas import schemas


router = APIRouter(prefix="/users", tags=["users"])


@router.Post('/register', response_model=schemas.UserCreate)
async def register(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    #checking if the user already exist
    existing_user = await db.execute(
        select(User).where(User.username == user.username) 

      ).scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    user_db = User(
        username=body.username,
        display_name=body.display_name,
        hashed_password=hash_password(body.password),
    )
    await db.add(user)
    await db.commit()
    await db.refresh(user)