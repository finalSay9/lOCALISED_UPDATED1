from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.schemas import schemas


router = APIRouter(prefix="/users", tags=["users"])


@router.Post('/register', response_model=schemas.UserCreate)
async def register(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    #checking if the user already exist
    existing_user = await db.execute()