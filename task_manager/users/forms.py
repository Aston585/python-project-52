from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserCreation(UserCreationForm):
    """Site user creation form."""

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username')
