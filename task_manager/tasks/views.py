from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from task_manager.mixins import LoginRequiredCustomMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class TasksListVew(LoginRequiredCustomMixin, ListView):
    template_name = 'tasks/tasks_list.html'
    model = Task


class TasksCreateView(LoginRequiredCustomMixin, CreateView):
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list_tasks')
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TasksUpdateView(LoginRequiredCustomMixin, UpdateView):
    pass


class TasksDeleteView(LoginRequiredCustomMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Task
    success_url = reverse_lazy('tasks:list_tasks')


class TaskDetailView(LoginRequiredCustomMixin, DetailView):
    pass
