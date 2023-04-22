# Imports
from fastapi import FastAPI
import uvicorn


# Routes imports
from routes import query_route


# Application
app = FastAPI()


# Home endpoint
@app.get("/", tags=["Home"])
async def home():
    return {"message": "Welcome to Home!"}


# Query parameters routes
app.include_router(query_route)


# Run main application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
