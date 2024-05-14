from django import forms
from django.contrib.auth.views import get_user_model
# from django.utils.translation import gettext_lazy as _


class UserCreateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
        ]
