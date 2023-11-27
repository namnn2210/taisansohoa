# user_router.py
from fastapi import APIRouter, HTTPException
from models import User
import user_auth

router = APIRouter()


@router.post("/register/")
async def register(user: User):
    user_auth.register(user.username, user.password)
    return {"message": "User registered successfully"}


@router.post("/login/")
async def login(user: User):
    if user_auth.login(user.username, user.password):
        return {"message": "Login successful."}
    else:
        raise HTTPException(
            status_code=401, detail="Incorrect username or password.")
