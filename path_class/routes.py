# Imports
from fastapi import APIRouter
from fastapi import Query, Path

from typing import Annotated


# Router
path_class_router = APIRouter(prefix="/pathclass", tags=["Path_Class"])


# Get route with path class
@path_class_router.get("/{path}")
def get_path_class(
    q: Annotated[str | None, Query()], path: Annotated[str | None, Path()]
):
    return {
        "query": f"This is a query parameter: {q}",
        "path": f"This is a path parameter: {path}",
    }


# Get route with metadata
@path_class_router.get("/metadata/{path}")
def get_metadata(
    path: Annotated[
        str,
        Path(title="title", description="description", deprecated=False),
    ],
    q: Annotated[str | None, Query()] = None,
):
    return {
        "query": f"This is a query parameter: {q}",
        "path": f"This is a path parameter: {path}",
    }


# Get route with number validation greater than
@path_class_router.get("/numbervalidation/gt/{path}")
def get_number_gt(
    path: Annotated[
        int,
        Path(title="title", description="description", deprecated=False, gt=2),
    ]
):
    return {"message": f"This number is greater than 2: {path}"}


# Get route with number validation greater than or equal to
@path_class_router.get("/numbervalidation/ge/{path}")
def get_number_ge(
    path: Annotated[
        int,
        Path(title="title", description="description", deprecated=False, ge=2),
    ]
):
    return {"message": f"This number is greater than or equal to 2: {path}"}


# Get route with number validation less than
@path_class_router.get("/numbervalidation/lt/{path}")
def get_number_lt(
    path: Annotated[
        float,
        Path(title="title", description="description", deprecated=False, lt=2.01),
    ]
):
    return {"message": f"This number is less than 2.01: {path}"}


# Get route with number validation less than or equal to
@path_class_router.get("/numbervalidation/le/{path}")
def get_number_le(
    path: Annotated[
        float,
        Path(title="title", description="description", deprecated=False, le=2.01),
    ]
):
    return {"message": f"This number is less than or equal to 2.01: {path}"}