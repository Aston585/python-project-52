from django import forms
from task_manager.tasks.models import Task
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'executor',
            'status',
            'labels',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Name')}),
            'description': forms.Textarea(
                attrs={'placeholder': _('Description')}
            ),
            'executor': forms.Select(attrs={'placeholder': _('Executor')}),
            'status': forms.Select(attrs={'placeholder': _('Status')}),
            'labels': forms.SelectMultiple(attrs={'placeholder': _('Labels')}),
        }

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'executor': _('Executor'),
            'status': _('Status'),
            'labels': _('Labels'),
        }
