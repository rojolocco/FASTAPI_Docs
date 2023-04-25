# Imports
from fastapi import APIRouter
from fastapi import Path, Query, Body

from typing import Annotated

# Import Models
from models import BodyModelType1, BodyModelType2


# Router
multi_params_router = APIRouter(prefix="/multiparams", tags=["Multiple_Parameters"])


# Get route multiple parameters
@multi_params_router.get("/")
async def get_multi_params():
    return {"message": "Welcome to multiple parameters!"}


# Post route multiple path parameters
@multi_params_router.post("/{path1}/{path2}")
async def post_multi_params(path1: Annotated[str, Path()], path2: Annotated[str, Path()]):
    return {
        "path_1": f"This is a path parameter: {path1}",
        "path_2": f"This is a path parameter: {path2}",
    }
