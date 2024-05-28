from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.schemas import ToDoListDTO, ToDoListPostDTO
from api.dependencies.database import get_session
from services.todolist import select_todo_by_id, insert_data_to_db, update_todo_with_put, delete_data_from_db


router = APIRouter()


@router.post("/new_todo/")
async def post_create_new_todo(
    session: Annotated[AsyncSession, Depends(get_session)], data: ToDoListPostDTO
):
    try:
        await insert_data_to_db(session, data)
        return {"msg": "Data insert"}
    except:
        return {"msg error": "Data not insert"}


@router.get("/todo/{todo_id}/", response_model=ToDoListDTO)
async def get_todo_by_id(
    todo_id: int, session: Annotated[AsyncSession, Depends(get_session)]
):
    result = await select_todo_by_id(todo_id, session)

    if result is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="По указаному id нечиго не найдено [!]"
        )

    return ToDoListDTO.model_validate(result, from_attributes=True)


@router.put("/todo_update_put/{todo_id}/")
async def put_todo(
    todo_id: int,
    data: ToDoListPostDTO,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    if await select_todo_by_id(todo_id, session) is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail="По указаному id нечиго не найдено [!]"
        )
    try:
        await update_todo_with_put(todo_id, session, data)
        return {"msg": "Data update"}
    except:
        return {"msg error": "Data not update"}


@router.delete('/delete/{todo_id}/')
async def delete_todo(todo_id: int, session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        await delete_data_from_db(session, todo_id)
        return {"msg": "Data delete"}
    except:
        return {"msg error": "Data not delete"}

