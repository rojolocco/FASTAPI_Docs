# Imports
from fastapi import APIRouter


# Router
router = APIRouter(prefix="/router", tags=["Router"])


# Router endpoint
@router.get("/")
def get_router():
    return {"message": "Welcome to router"}
