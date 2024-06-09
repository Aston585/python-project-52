from django.test import TestCase
from task_manager.statuses.models import Status
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestStatusUpdate(TestCase):
    fixtures = ['db_statuses.json', 'db_user.json']

    def test_status_update(self):
        new_status = {'name': 'Finish'}
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        self.client.post(
            reverse('statuses:update_status', kwargs={'pk': 1}),
            new_status
        )
        update_status = Status.objects.get(pk=1)
        self.assertEqual(update_status.name, new_status['name'])
