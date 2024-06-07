from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Statuses


class TestStatusCreate(TestCase):

    def test_status_create(self):
        fixture = 'Start'
        self.client.post(reverse('statuses:create_status'), fixture)
        status = Statuses.objects.get(kwargs={'pk': 1})
        self.assertEqual(status.name, fixture)
