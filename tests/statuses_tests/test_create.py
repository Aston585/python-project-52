from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model


class TestStatusCreate(TestCase):
    fixtures = ['db_user.json']

    def test_status_create(self):
        fixture = {'name': 'Start'}
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        self.client.post(reverse('statuses:create_status'), fixture)
        status = Status.objects.get(pk=1)
        self.assertEqual(status.name, fixture['name'])
