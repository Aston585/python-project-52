from django import forms
from django.contrib.auth.models import User as UserModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator


class UserCreateForm(forms.ModelForm):
    password_min_len = 3
    warning_password_min_len = _(
        "The entered password is too short. "
        "It must contain at least 3 characters."
    )

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(),
        help_text=_(
            "<ul>"
            "<li>Your password must contain at least 3 characters.</li>"
            "</ul>"
        ),
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        validators=[
            MinLengthValidator(password_min_len,
                               message=warning_password_min_len),
        ],
        widget=forms.PasswordInput(),
        help_text=_("Re-enter your password again, please."),
    )

    class Meta:
        model = UserModel
        fields = [
            "first_name",
            "last_name",
            "username",
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("Passwords don't match"), code='invalid')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
