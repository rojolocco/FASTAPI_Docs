# Imports
from fastapi import APIRouter
from typing import Union

# Route for path parameters
query_route = APIRouter(prefix="/queryparameters", tags=["Query_Parameters"])


# Get Routes
@query_route.get("/")
async def get_query(q):
    return {"message": f"This is a query parameter: {q}"}


# Get Routes with one default values
@query_route.get("/defaultvalue/one")
async def get_query_with_one_default_value(q: str | None = None):
    return {"message": f"This is a query parameter: {q}"}


# Get Routes with two default values
@query_route.get("/defaultvalue/two")
async def get_query_with_two_default_value(q: str | None = None, p: bool = False):
    if p:
        return {"message": f"p is a boolean query parameter: {p}"}
    return {"message": f"This is a query parameter: {q}"}


# Get Routes with one required parameter
@query_route.get("/requiredvalue/one")
async def get_query_with_one_required_value(q: str | None):
    return {"message": f"This is a required query parameter: {q}"}


# Get Routes with two required parameter
@query_route.get("/requiredvalue/two")
async def get_query_with_two_required_value(q: str | None, p: bool):
    if p:
        return {"message": f"p is a boolean query parameter: {p}"}
    return {"message": f"This is a required query parameter: {q}"}
