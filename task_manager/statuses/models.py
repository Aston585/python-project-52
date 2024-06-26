from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
