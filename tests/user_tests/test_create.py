from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import json
from os.path import join
from task_manager.settings import FIXTURE_DIRS


class UserCreateTest(TestCase):

    def load_fixture(self):
        fixture_user_create = join(FIXTURE_DIRS[0], 'user_create.json')
        with open(fixture_user_create, 'r') as f:
            return json.load(f)

    def test_user_create(self):
        fixture = self.load_fixture()
        self.client.post(reverse('users:create_user'), fixture)
        new_user = get_user_model().objects.filter(
            username=fixture.get('username')
            ).first()
        self.assertEqual(
            new_user.username,
            fixture.get('username')
        )
