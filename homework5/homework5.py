# Задание
#
# Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
#
# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
#
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.
from typing import List

from fastapi import FastAPI,Query,HTTPException,Form
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
class UpdateTask(BaseModel):
    title: str
    description: str

current_id = 1
app = FastAPI()
tasks = []


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return tasks


@app.get("/tasks/{task_id}",response_model=Task)
async def read_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
@app.post("/tasks/",response_model=Task)
async def create_task(
    title: str = Form(...),
    description: str = Form(...),
):
    global current_id
    task = Task(id=current_id, title=title, description=description)
    tasks.append(task)
    current_id += 1
    return task
@app.put("/tasks/{task_id}",response_model=Task)
async def update_task(task_id: int,updated_task: UpdateTask):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    return task
@app.delete("/tasks/{task_id}", response_model=List[Task])
async def delete_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task)
    return tasks