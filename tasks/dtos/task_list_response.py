from pydantic import BaseModel

from ..dtos.task_response import TaskResponse


class TaskListResponse(BaseModel):
    tasks: list[TaskResponse]
