from typing import List
from fastapi import APIRouter, status, HTTPException
from prisma import Prisma
from src.models.user_model import User

db = Prisma()
authRoute = APIRouter()

@authRoute.post("/register")
async def register_user(user: User):
    """
    Register a new user.
    """
    try:
        await db.connect()
        new_user = await db.user.create(
            data = {
                "email": user.email,
                "password": user.password,
            }
        )
        return {"message": "User registered successfully", "user": new_user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        await db.disconnect()

@authRoute.post("/login")
async def login_user(user: User):
    """
    Login a user.
    """
    try:
        await db.connect()
        existing_user = await db.user.find_first(
            where={
                "email": user.email,
                "password": user.password,
            }
        )
        if not existing_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return {"message": "User logged in successfully", "user": existing_user}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        await db.disconnect()

