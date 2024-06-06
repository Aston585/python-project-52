from django.db import models


class Statuses(models.Model):
    name = models.CharField(max_length=30, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
