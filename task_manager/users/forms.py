from django import forms
from django.contrib.auth.views import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator


class UserCreateForm(forms.ModelForm):
    password_min_len = 3

    password1 = forms.CharField(
        validators=[
            MinLengthValidator(password_min_len,
                               _("Password is too short"))],
        label=_('Password'),
        widget=forms.PasswordInput(),
        help_text=_("Your password should be at least 3 symbols long."),
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        validators=[
            MinLengthValidator(password_min_len,
                               _("Password is too short")),
        ],
        widget=forms.PasswordInput(),
        help_text=_("Re-enter your password again, please."),
    )

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
        ]
