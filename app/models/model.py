
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from db.database import Base



class ToDoListOrm(Base):
    __tablename__ = 'ToDoList'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(32))
    description: Mapped[str]
    completed: Mapped[bool]
