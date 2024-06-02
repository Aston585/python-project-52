from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserCreateTest(TestCase):
    fixtures = ['user.json']

    def test_user_create(self):
        response = self.client.post(reverse("create_user"), self.fixtures)
        new_user = get_user_model().objects.get(pk=1)
        self.assertEqual(new_user.username, response.get('username'))
