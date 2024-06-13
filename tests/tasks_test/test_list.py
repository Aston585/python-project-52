from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class TaskListTest(TestCase):
    fixtures = ['db_task.json']

    def test_task_list(self):
        author = get_user_model().objects.get(pk=1)
        self.client.force_login(author)
        responce = self.client.get(reverse('tasks:list_tasks'))
        self.assertEqual(responce.status_code, 200)
