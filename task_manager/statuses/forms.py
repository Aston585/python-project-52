from django import forms
from task_manager.statuses.models import Statuses


class StatusForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
        widgets = {
            "name": forms.TextInput()
        }

