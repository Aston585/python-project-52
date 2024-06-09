from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserDeleteTest(TestCase):
    fixtures = ['db_user.json']

    def test_user_delete(self):
        user = get_user_model().objects.all().first()
        self.client.force_login(user)
        self.client.post(reverse("users:delete_user", kwargs={'pk': 1}))
        db_users = get_user_model().objects.all()
        self.assertNotIn(user, db_users)
