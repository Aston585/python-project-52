from django import forms
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        widgets = {"name": forms.TextInput(attrs={'plaseholder': _('Name')})}
        labels = {"name": _('Name')}
