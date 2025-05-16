from queue.celery import app

@app.task
def example_task(x, y):
    return x + y