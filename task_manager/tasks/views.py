from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from task_manager.mixins import LoginRequiredCustomMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect


class TasksListVew(LoginRequiredCustomMixin, ListView):
    template_name = 'tasks/tasks_list.html'
    model = Task


class TaskCreateView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = 'tasks/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list_tasks')
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:list_tasks')
    success_message = _('Task modified successfully')


class TaskDeleteView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = 'tasks/task_delete.html'
    model = Task
    success_url = reverse_lazy('tasks:list_tasks')
    success_message = _('Task deleted successfully')
    error_message = _('Only its author can delete a task')

    def get(self, request, *args, **kwargs):
        curent_task = self.get_object()
        if curent_task.author != request.user:
            messages.error(self.request, self.error_message)
            return redirect(self.success_url)
        self.object = self.get_object()
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
