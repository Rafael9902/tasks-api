from pydantic import BaseModel, Field


class CreateTaskRequest(BaseModel):
    description: str = Field(..., max_length=255)
    created_by: int = Field(..., description="User ID of the task creator")
