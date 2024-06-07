from django.test import TestCase
from task_manager.statuses.models import Statuses
from django.urls import reverse


class TestStatusUpdate(TestCase):
    fixtures = ['db_statuses.json']

    def test_status_update(self):
        new_status = 'Finish'
        self.client.post(reverse('statuse:update_status', new_status))
        update_status = Statuses.objects.get(kwargs={'pk': 1})
        self.assertEqual(update_status.name, new_status)
