# Imports
from fastapi import APIRouter


# Router
router = APIRouter(prefix="/routes", tags=["Routes"])


# Get Routes
@router.get("/")
def get_route():
    return {"message": "Welcome to routes!"}
