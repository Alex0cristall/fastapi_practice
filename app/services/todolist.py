from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete

from models.model import ToDoListOrm
from schemas.schemas import ToDoListPostDTO


async def insert_data_to_db(session: AsyncSession, data: ToDoListPostDTO):
    result = ToDoListOrm(**data.model_dump())
    session.add(result)
    await session.commit()


async def select_todo_by_id(todo_id: int, session: AsyncSession):
    result = await session.get(ToDoListOrm, todo_id)
    return result


async def update_todo_with_put(
    todo_id: int, session: AsyncSession, data: ToDoListPostDTO
):
    stmt = update(ToDoListOrm).filter_by(id=todo_id).values(data.model_dump())
    await session.execute(stmt)
    await session.commit()


async def delete_data_from_db(session: AsyncSession, todo_id: int):
    stmt = (
        delete(ToDoListOrm).filter_by(id=todo_id)
    )
    await session.execute(stmt)
    await session.commit()
