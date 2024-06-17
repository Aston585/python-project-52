from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class TaskListTest(TestCase):
    fixtures = ['db_task.json']

    def test_task_list(self):
        author = get_user_model().objects.get(pk=1)
        self.client.force_login(author)
        response = self.client.get(reverse('tasks:list_tasks'))
        self.assertEqual(response.status_code, 200)
        tasks = response.context['task_list']
        self.assertEqual(tasks.count(), 3)

        data_filter = {
            'labels': 2,
            'executor': 2
        }
        response = self.client.get(reverse('tasks:list_tasks'), data_filter)
        self.assertEqual(response.status_code, 200)
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 2)

        self.client.get(reverse('tasks:list_tasks'))
        data_filter = {
            'tasks_created_by_me': True
        }
        response = self.client.get(reverse('tasks:list_tasks'), data_filter)
        self.assertEqual(response.status_code, 200)
        tasks = response.context['object_list']
        self.assertEqual(tasks.count(), 2)
