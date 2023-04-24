# Imports
from fastapi import APIRouter
from fastapi import Query

from typing import Annotated


# Router
query_class_router = APIRouter(prefix="/queryclass", tags=["Query_Class"])


# Get route with Query class
@query_class_router.get("/")
def get_query_class(q: Annotated[str, Query()] = None):
    return {"message": f"This is a query parameter: {q}"}


# Get route with max length validator
@query_class_router.get("/maxlength")
def get_query_max_length(q: Annotated[str, Query(max_length=5)] = None):
    return {"message": f"This is a query parameter: {q}"}


# Get route with min length validator
@query_class_router.get("/minlength")
def get_query_min_length(q: Annotated[str, Query(min_length=2)] = None):
    return {"message": f"This is a query parameter: {q}"}


# Get route with required value
@query_class_router.get("/required")
def get_required_query(q: Annotated[str, Query()]):
    return {"message": f"This is a required query parameter: {q}"}


# Get route with required value with Ellipsis
@query_class_router.get("/requiredwithellipsis")
def get_required_with_ellipsis_query(q: Annotated[str, Query()] = ...):
    return {"message": f"This is a required query parameter: {q}"}


# Get route with list of query values
@query_class_router.get("/list")
def get_list(q: Annotated[list[str] | None, Query()]):
    return {"message": f"This is a list of query parameters: {q}"}


# Get route with list of query values and two predifined values
@query_class_router.get("/list/predefined")
def get_list_predifined(q: Annotated[list[str] | None, Query()] = ["str1", "str2"]):
    return {"message": f"This is a list of query parameters: {q}"}


# Get rote with metadata
@query_class_router.get("/metadata")
def get_metadata(
    q: Annotated[
        list[str] | None,
        Query(title="title", description="descrption", alias="alias", deprecated=True),
    ]
):
    return {"message": f"This is a list of query parameters: {q}"}
