from django.test import TestCase
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from task_manager. statuses.models import Status
from django.urls import reverse


class TaskUpdateTest(TestCase):
    fixtures = ['db_task.json']

    def test_task_update(self):
        author = get_user_model().objects.get(pk=1)
        executor = get_user_model().objects.get(pk=2)
        status = Status.objects.get(pk=1)
        self.client.force_login(author)
        data_update = {
            'name': 'Kill Tatarin',
            'description': 'Kill Tatarin in market',
            'executor': executor.id,
            'status': status.id
        }
        url = reverse('tasks:update_task', kwargs={'pk': 1})
        self.client.post(url, data_update)
        new_executor = Task.objects.get(pk=1).executor
        self.assertEqual(new_executor.id, executor.id)
