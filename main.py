# main.py
from fastapi import FastAPI
from user_router import router as user_router
from ncc_router import router as ncc_router
from pb_router import router as pb_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(ncc_router, prefix="/ncc", tags=["ncc"])
app.include_router(pb_router, prefix="/pb", tags=["pb"])
