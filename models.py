from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    password: str


class NCC(BaseModel):
    MANCC: Optional[str] = None  # Optional during creation
    TenNCC: str
    SDT: str
    EMAIL: str
    MST: str
    DC: str


class PB(BaseModel):
    MAPB: str
    TenPB: str
