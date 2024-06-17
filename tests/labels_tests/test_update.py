from django.test import TestCase
from task_manager.labels.models import Label
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestLabelUpdate(TestCase):
    fixtures = ['db_labels.json', 'db_user.json']

    def test_status_update(self):
        new_label = {'name': 'Super label'}
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        url = reverse('labels:update_label', kwargs={'pk': 1})
        self.client.post(url, new_label)
        update_label = Label.objects.get(pk=1)
        self.assertEqual(update_label.name, new_label['name'])
