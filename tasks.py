from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from ..services.category_service.py import CategoryService
from ..services.task_service import TaskService

router = APIRouter()

class Category(BaseModel):
    id: int
    title: str
    description: str

@router.post('/update_index')
def update_index(categories: list[Category], background_tasks: BackgroundTasks):
    task_id = 'update_index_task'
    background_tasks.add_task(CategoryService.update_category_index, categories, task_id)
    return {"task_id": task_id}

@router.get('/task_status/{task_id}')
def task_status(task_id: str):
    status = TaskService.get_status(task_id)
    if not status:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task_id": task_id, "status": status}
