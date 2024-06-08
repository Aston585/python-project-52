from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Statuses
from task_manager.statuses.forms import StatusForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import LoginRequiredCustomMixin
from django.contrib import messages
from django.shortcuts import redirect


class ListStatusesView(
    LoginRequiredCustomMixin,
    ListView,
):
    template_name = 'statuses/status_list.html'
    model = Statuses


class StatusesCreateView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = 'statuses/status_create.html'
    model = Statuses
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list_statuses')
    success_message = _('Status successfully created')


class StatusUpdateView(
    LoginRequiredCustomMixin,
    UpdateView,
):
    template_name = 'statuses/status_update.html'
    model = Statuses
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list_statuses')
    success_message = _('Status successfully changed')


class StatusDeleteView(
    LoginRequiredCustomMixin,
    DeleteView,
):
    template_name = 'statuses/status_delete.html'
    model = Statuses
    success_url = reverse_lazy('statuses:list_statuses')
    success_message = _('Status successfully deleted')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(
                request,
                _('Cannot delete status because it is in use')
            )
            return redirect(self.success_url)
        return super().delete(request, *args, **kwargs)
