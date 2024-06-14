from django import forms
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        widgets = {"name": forms.TextInput(attrs={'plaseholder': _('Name')})}
        labels = {"name": _('Name')}
