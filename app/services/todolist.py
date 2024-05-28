from sqlalchemy.ext.asyncio import AsyncSession

from models.model import ToDoListOrm
from schemas.schemas import ToDoListPostDTO



async def select_todo_by_id(todo_id: int, session: AsyncSession):
    result = await session.get(ToDoListOrm, todo_id)
    return result

async def update_todo_with_put(
        todo_id: int,
        session: AsyncSession,
        data: ToDoListPostDTO
):
    todo = await session.get(ToDoListOrm, todo_id)
    # todo.
