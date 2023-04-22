# Imports
from fastapi import FastAPI
import uvicorn


# Import routes
from routes import router


# Application
app = FastAPI()


# Home endpoint
@app.get("/", tags=["Home"])
async def home():
    return {"message": "Welcome to Home!"}


# Routers
app.include_router(router)


# Run main application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
