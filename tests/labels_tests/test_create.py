from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model


class TestLabelCreate(TestCase):
    fixtures = ['db_user.json']

    def test_status_create(self):
        fixture = {'name': 'Black label'}
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        self.client.post(reverse('labels:create_label'), fixture)
        label = Label.objects.get(pk=1)
        self.assertEqual(label.name, fixture['name'])
