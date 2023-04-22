# Imports
from fastapi import APIRouter

# Imports predifined values classes
from enum_values import DaysOfTheWeek, MonthOfYear


# Route for path parameters
path_route = APIRouter(prefix="/pathparameters", tags=["Path_Parameters"])


# Get Routes
@path_route.get("/withouttype/{item}")
async def get_without_type(item):
    return {"message": f"This route without types: The path parameters is {item}"}


# Get Route with int type
@path_route.get("/withtype/type/int/{item}")
async def get_without_type(item: int):
    return {"message": f"The path parameters is the intenger: {item}"}


# Get Route with float type
@path_route.get("/withtype/type/float/{item}")
async def get_without_type(item: float):
    return {"message": f"The path parameters is the float: {item}"}


# Get Route with str type
@path_route.get("/withtype/type/str/{item}")
async def get_without_type(item: str):
    return {"message": f"The path parameters is the string: {item}"}


# Get Route with bool type
@path_route.get("/withtype/type/bool/{item}")
async def get_without_type(item: bool):
    return {"message": f"The path parameters is the boolian: {item}"}


# Get Route with predifined day value
@path_route.get("/withenum/predifined/{day}")
async def get_day_of_the_week(day: DaysOfTheWeek):
    return {"message": f"Predifined values: Today is {day}"}


# Get Route with predifined month value
@path_route.get("/withenum/predifined/{month}")
async def get_month(month: MonthOfYear):
    return {"message": f"Predifined values: Month number is {month}"}
