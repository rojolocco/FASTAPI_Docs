# Imports
from fastapi import APIRouter


# Import models
from models import RequestBodyModel


# Router
request_body_router = APIRouter(prefix="/requestbody", tags=["Request_Body"])


# Post route
@request_body_router.post("/")
def get_route(body: RequestBodyModel):
    return body


# Post route with path parameters
@request_body_router.post("/{path}")
def get_path_body(path: str, body: RequestBodyModel):
    return {
        "message": f"This is a path parameter: {path}. This is the request body: {body.dict()}"
    }


# Post route with query parameters
@request_body_router.post("/query")
def get_query_body(query: str, body: RequestBodyModel):
    return {
        "message": f"This is a path parameter: {query}. This is the request body: {body.dict()}"
    }


# Post route with query and path parameters
@request_body_router.post("/queryandpath/{path}")
def get_query_path_body(path: int, query: str, body: RequestBodyModel):
    return {
        "path": f"This is a path parameter: {path}",
        "query": f"This is a path parameter: {query}",
        "body": f"This is the request body: {body.dict()}",
    }

