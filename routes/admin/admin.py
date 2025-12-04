from fastapi import APIRouter
from models import schemas

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

@router.post("/login")
async def login(body : schemas.AdminBase):
    return

