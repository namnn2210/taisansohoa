from fastapi import APIRouter, HTTPException
import uuid
import process
from models import NCC

router = APIRouter()


@router.post("/", response_model=NCC)
async def create_ncc(ncc: NCC):
    ncc.MANCC = str(uuid.uuid4())  # Generate a unique ID
    created_ncc = process.create_ncc(ncc)
    if created_ncc:
        return created_ncc
    raise HTTPException(status_code=500, detail="Error creating NCC")


@router.get("/{mancc}", response_model=NCC)
async def read_ncc(mancc: str):
    ncc = process.get_ncc(mancc)
    if ncc:
        return ncc
    raise HTTPException(status_code=404, detail="NCC not found")


@router.put("/{mancc}", response_model=NCC)
async def update_ncc(mancc: str, ncc: NCC):
    updated_ncc = process.update_ncc(mancc, ncc)
    if updated_ncc:
        return updated_ncc
    raise HTTPException(status_code=404, detail="NCC not found")


@router.delete("/{mancc}", response_model=NCC)
async def delete_ncc(mancc: str):
    deleted_ncc = process.delete_ncc(mancc)
    if deleted_ncc:
        return deleted_ncc
    raise HTTPException(status_code=404, detail="NCC not found")
