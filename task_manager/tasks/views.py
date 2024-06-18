from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from task_manager.mixins import LoginRequiredCustomMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django_filters.views import FilterView
from task_manager.tasks.filters import TaskFilter


class TasksListVew(
    LoginRequiredCustomMixin,
    FilterView,
):
    template_name = 'tasks/tasks_list.html'
    filterset_class = TaskFilter


class TaskCreateView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = 'form_create_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list_tasks')
    success_message = _('Task created successfully')
    extra_context = {
        'header': _('Create task'),
        'button': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    template_name = 'form_create_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list_tasks')
    success_message = _('Task modified successfully')
    extra_context = {
        'header': _('Task change'),
        'button': _('Change'),
    }


class TaskDeleteView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = 'form_delete.html'
    model = Task
    success_url = reverse_lazy('tasks:list_tasks')
    success_message = _('Task deleted successfully')
    error_message = _('Only its author can delete a task')
    extra_context = {
        'header': _('Remove task'),
    }

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            messages.error(self.request, self.error_message)
            return redirect(self.success_url)
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, self.success_message)
        return redirect(success_url)


class TaskDetailView(LoginRequiredCustomMixin, DetailView):
    template_name = 'tasks/task_detail.html'
    model = Task
