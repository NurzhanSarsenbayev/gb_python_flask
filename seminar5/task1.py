# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
from typing import Optional, List

from fastapi import FastAPI, HTTPException, Request, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./seminar5/templates")

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: bool

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str]
    status: bool

# Глобальный счетчик для идентификаторов задач
current_id = 1
tasks = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {
        "request": request,
        "title": "Task Management",
        "description": "Manage your tasks efficiently",
    }
    return templates.TemplateResponse("index.html", context)

@app.post("/tasks", response_model=Task)
async def create_task(
    title: str = Form(...),
    description: Optional[str] = Form(None),
    status: bool = Form(False)
):
    global current_id
    task = Task(id=current_id, title=title, description=description, status=status)
    tasks.append(task)
    current_id += 1  # Увеличиваем счетчик
    return task

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    for i, existing_task in enumerate(tasks):
        if existing_task.id == task_id:
            updated_task = Task(id=task_id, **task_update.dict())
            tasks[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    for i, existing_task in enumerate(tasks):
        if existing_task.id == task_id:
            deleted_task = tasks.pop(i)
            return deleted_task
    raise HTTPException(status_code=404, detail="Task not found")