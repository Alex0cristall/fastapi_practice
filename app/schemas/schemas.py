from pydantic import BaseModel




class ToDoListPostDTO(BaseModel):
    title: str
    description: str
    completed: bool = False

class ToDoListDTO(ToDoListPostDTO):
    id: int
