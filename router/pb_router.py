# pb_router.py
from fastapi import APIRouter, HTTPException
from models import PB
import process  # This module should contain the actual database interaction logic

router = APIRouter()


@router.post("/", response_model=PB)
async def create_pb(pb: PB):
    try:
        created_pb = process.create_pb(pb)
        return created_pb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{mapb}", response_model=PB)
async def get_pb(mapb: str):
    try:
        pb = process.get_pb(mapb)
        if pb is None:
            raise HTTPException(status_code=404, detail="PB not found")
        return pb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{mapb}", response_model=PB)
async def update_pb(mapb: str, pb: PB):
    try:
        updated_pb = process.update_pb(mapb, pb)
        if updated_pb is None:
            raise HTTPException(status_code=404, detail="PB not found")
        return updated_pb
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{mapb}")
async def delete_pb(mapb: str):
    try:
        success = process.delete_pb(mapb)
        if not success:
            raise HTTPException(status_code=404, detail="PB not found")
        return {"message": "PB deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
