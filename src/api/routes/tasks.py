from fastapi import APIRouter, HTTPException
from queue.celery import app as celery_app

router = APIRouter()

@router.post("/tasks/")
def submit_task(x: int, y: int):
    try:
        # Submit the task to the Celery queue
        task = celery_app.send_task("queue.tasks.example_task", args=[x, y])
        return {"task_id": task.id, "status": "Task submitted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))