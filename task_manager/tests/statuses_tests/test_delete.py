from django.test import TestCase
from task_manager.statuses.models import Statuses
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestStatusDelete(TestCase):
    fixtures = ['db_statuses.json', 'db_user.json']

    def test_status_update(self):
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        self.client.post(reverse('statuses:delete_status', kwargs={'pk': 1}))
        statuses = Statuses.objects.all()
        self.assertEqual(statuses.count(), 0)
