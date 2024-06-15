from django.test import TestCase
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from django.urls import reverse


class TaskDeleteTest(TestCase):
    fixtures = ['db_task.json']

    def test_task_delete(self):
        author = get_user_model().objects.get(pk=1)
        self.client.force_login(author)
        self.client.post(reverse('tasks:delete_task', kwargs={'pk': 1}))
        self.assertEqual(Task.objects.count(), 2)
