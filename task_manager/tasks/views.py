from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from task_manager.mixins import LoginRequiredCustomMixin


class TasksListVew(LoginRequiredCustomMixin, ListView):
    pass


class TasksCreateView(LoginRequiredCustomMixin, CreateView):
    pass


class TasksUpdateView(LoginRequiredCustomMixin, UpdateView):
    pass


class TasksDeleteView(LoginRequiredCustomMixin, DeleteView):
    pass


class TaskDetailView(LoginRequiredCustomMixin, DetailView):
    pass
