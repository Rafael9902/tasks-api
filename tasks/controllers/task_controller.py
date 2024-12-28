from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pydantic import ValidationError
from tasks.services.task_service import TaskService
from tasks.dtos.create_task_request import CreateTaskRequest
from tasks.dtos.task_response import TaskResponse
from tasks.dtos.task_list_response import TaskListResponse


class TaskController(APIView):
    def post(self, request):
        try:
            task_data = CreateTaskRequest(**request.data)
            task = TaskService.create_task(task_data.model_dump())

            response = TaskResponse(
                id=task.id,
                description=task.description,
                created_at=task.created_at.isoformat(),
                updated_at=task.updated_at.isoformat(),
                created_by=task.created_by.id,
                is_active=task.is_active,
            )
            return Response(response.model_dump(), status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        tasks = TaskService.get_all_tasks()

        task_responses = [
            TaskResponse(
                id=task.id,
                description=task.description,
                created_at=task.created_at.isoformat(),
                updated_at=task.updated_at.isoformat(),
                created_by=task.created_by.id,
                is_active=task.is_active,
            )
            for task in tasks
        ]
        response = TaskListResponse(tasks=task_responses)
        return Response(response.dict(), status=status.HTTP_200_OK)
