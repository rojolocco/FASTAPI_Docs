# Imports
from pydantic import BaseModel


# Body Model Type 1
class BodyModelType1(BaseModel):
    number: int
    boolean: bool = True


# Body Model Type 2
class BodyModelType2(BaseModel):
    number: float
    boolean: bool = False