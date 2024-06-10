from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from task_manager.mixins import LoginRequiredCustomMixin
from task_manager.tasks.models import Task


class TasksListVew(LoginRequiredCustomMixin, ListView):
    template_name = 'tasks/tasks_list.html'
    model = Task


class TasksCreateView(LoginRequiredCustomMixin, CreateView):
    pass


class TasksUpdateView(LoginRequiredCustomMixin, UpdateView):
    pass


class TasksDeleteView(LoginRequiredCustomMixin, DeleteView):
    pass


class TaskDetailView(LoginRequiredCustomMixin, DetailView):
    pass
