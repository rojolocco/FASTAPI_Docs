# Imports
from fastapi import FastAPI
import uvicorn


<<<<<<< HEAD
# Import routers
=======
# Import routes
>>>>>>> master
from routes import router


# Application
app = FastAPI()


# Home endpoint
@app.get("/", tags=["Home"])
async def home():
    return {"message": "Welcome to Home!"}


<<<<<<< HEAD
# Include routes
=======
# Routers
>>>>>>> master
app.include_router(router)


# Run main application
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
