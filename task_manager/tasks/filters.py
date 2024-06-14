import django_filters
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_("Status")
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label=_("Executor")
    )
    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label"),
        widget=forms.Select,
    )
    tasks_created_by_me = django_filters.BooleanFilter(
        label=_("Only your tasks"),
        method="get_tasks_created_by_yourself",
        widget=forms.CheckboxInput,
    )

    def get_tasks_created_by_yourself(self, queryset, name, value):
        if value:
            return queryset.filter(author_id=self.request.user.id)
        return queryset

    class Meta:
        model = Task
        fields = ["status", "executor"]
