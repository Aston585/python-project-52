from django.db import models
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='tasks_with_this_executor'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='tasks_with_this_status'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='tasks_with_this_author',
        blank=False,
        null=False,
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
