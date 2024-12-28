from tasks.models.task import Task


class TaskRepository:
    @staticmethod
    def create_task(data):
        return Task.objects.create(**data)

    @staticmethod
    def get_all_tasks():
        return Task.objects.filter(is_active=True)

    @staticmethod
    def get_task_by_id(task_id):
        return Task.objects.filter(id=task_id, is_active=True).first()
