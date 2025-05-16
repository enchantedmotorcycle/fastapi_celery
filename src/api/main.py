from fastapi import FastAPI, HTTPException
from api.routes import router as api_router
from api.routes.tasks import router as tasks_router

app = FastAPI()

app.include_router(api_router)
app.include_router(tasks_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}

