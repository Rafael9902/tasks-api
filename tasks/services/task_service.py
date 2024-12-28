from tasks.repositories.task_repository import TaskRepository


class TaskService:
    @staticmethod
    def create_task(data):
        return TaskRepository.create_task(data)

    @staticmethod
    def get_all_tasks():
        return TaskRepository.get_all_tasks()

    @staticmethod
    def get_task_by_id(task_id):
        return TaskRepository.get_task_by_id(task_id)
