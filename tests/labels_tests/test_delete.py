from django.test import TestCase
from task_manager.labels.models import Label
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestLabelDelete(TestCase):
    fixtures = ['db_labels.json', 'db_user.json']

    def test_status_update(self):
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        self.client.post(reverse('labels:delete_label', kwargs={'pk': 1}))
        labels = Label.objects.all()
        self.assertEqual(labels.count(), 0)
