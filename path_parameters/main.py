# Imports
from fastapi import FastAPI
import uvicorn


#Routes imports
from routes import path_route

# Application
app = FastAPI()


# Home endpoint
@app.get("/",tags=["Home"])
async def home():
    return {"message": "Welcome to Home!"}


# Path parameters routes
app.include_router(path_route)


# Run main application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
