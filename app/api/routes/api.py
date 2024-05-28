from fastapi import APIRouter

from api.routes import todolist


router = APIRouter()
router.include_router(todolist.router, tags=['ToDoList'])
