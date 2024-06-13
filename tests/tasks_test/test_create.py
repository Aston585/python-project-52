from django.test import TestCase
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from task_manager. statuses.models import Status
from django.urls import reverse


class TaskCreateTest(TestCase):
    fixtures = ['db_task.json']

    def test_task_create(self):
        author = get_user_model().objects.get(pk=1)
        executor = get_user_model().objects.get(pk=2)
        status = Status.objects.get(pk=1)
        self.client.force_login(author)
        data_create = {
            'name': 'Protect Nemec',
            'description': 'Protect Nemec from the bandit',
            'executor': executor.id,
            'status': status.id
        }
        self.client.post(reverse('tasks:create_task'), data_create)
        self.assertEqual(Task.objects.count(), 2)
