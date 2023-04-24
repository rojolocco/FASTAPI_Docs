# Imports
from pydantic import BaseModel


# Request Body Model
class RequestBodyModel(BaseModel):
    intenger: int
    string: str
    float: float
    boolean: bool | None = None
