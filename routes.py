# Imports
from fastapi import APIRouter


# Router
<<<<<<< HEAD
router = APIRouter(prefix="/routes", tags=["Routes"])


# Get Routes
@router.get("/")
def get_route():
    return {"message": "Welcome to routes!"}
=======
router = APIRouter(prefix="/router", tags=["Router"])


# Router endpoint
@router.get("/")
def get_router():
    return {"message": "Welcome to router"}
>>>>>>> master
