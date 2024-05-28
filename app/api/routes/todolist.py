from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from models.model import ToDoListOrm
from schemas.schemas import ToDoListDTO, ToDoListPostDTO
from db.database import sync_session_fabric
from api.dependencies.database import get_session
from services.todolist import select_todo_by_id




router = APIRouter()


@router.post('/new_todo/')
async def post_create_new_todo(data: ToDoListPostDTO):
    with sync_session_fabric() as session:
        result = ToDoListOrm(**data.model_dump())
        session.add(result)
        session.commit()
    return {'msg': 'Nice!'}


@router.get('/todo/{todo_id}/', response_model=ToDoListDTO)
async def get_todo_by_id(todo_id: int, session: Annotated[AsyncSession, Depends(get_session)]):
    result = await select_todo_by_id(todo_id, session)

    if result is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail='По указаному id нечиго не найдено [!]'
        )

    return ToDoListDTO.model_validate(result, from_attributes=True)


@router.put('/todo_update_put/{todo_id}/')
async def put_todo(
    todo_id: int,
    todo: ToDoListPostDTO,
    session: Annotated[AsyncSession, Depends(get_session)]
):
    ...



