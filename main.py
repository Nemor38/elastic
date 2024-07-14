from fastapi import FastAPI
from .routers import category, tasks
from .models.category import CategoryIndex

app = FastAPI()

# Підключення роутерів
app.include_router(category.router)
app.include_router(tasks.router)

# Ініціалізація індексу
CategoryIndex.create_index()
