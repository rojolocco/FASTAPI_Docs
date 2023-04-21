# Imports
from fastapi import FastAPI
import uvicorn


# Application
app = FastAPI()


# Home endpoint
@app.get("/")
async def home():
    return {"message": "Welcome to Home!"}


# Run main application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
