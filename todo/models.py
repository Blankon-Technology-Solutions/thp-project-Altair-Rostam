from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE

from .utils import StatusEnum


class Todo(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="todo_owner", on_delete=CASCADE)
    status = models.IntegerField(choices=StatusEnum.choices, default=StatusEnum.UNCHECKED)

    def __str__(self):
        return f"{self.content} - {self.status}"
