from pydantic import BaseModel
from typing import Annotated


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int
    
    
class STaskId(BaseModel):
    ok: bool = True
    task_id: int