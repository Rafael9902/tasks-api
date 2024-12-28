from pydantic import BaseModel


class TaskResponse(BaseModel):
    id: int
    description: str
    created_at: str
    updated_at: str
    created_by: int
    is_active: bool
