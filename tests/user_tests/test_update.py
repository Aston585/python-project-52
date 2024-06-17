from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import json
from os.path import join
from task_manager.settings import FIXTURE_DIRS


class UserUpdateTest(TestCase):
    fixtures = ["db_user.json"]

    def load_fixture(self):
        fixture_user_update = join(FIXTURE_DIRS[0], "user_create.json")
        with open(fixture_user_update, "r") as f:
            return json.load(f)

    def test_user_update(self):
        fixture = self.load_fixture()
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        self.client.post(
            reverse("users:update_user", kwargs={"pk": 1}),
            fixture
        )
        up_user = get_user_model().objects.filter(
            username=fixture.get("username"),
        )
        self.assertEqual(up_user.username.first(), fixture.get("username"))
