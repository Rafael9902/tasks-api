from django.db.models import TextField, BooleanField, DateTimeField, Model


class Task(Model):
    description = TextField()
    created_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.description
