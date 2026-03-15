from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas import schemas


router = APIRouter(prefix="/users", tags=["users"])


@router.Post('/register', response_model=schemas.UserCreate)
async def register(user: UserCreate, )