from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Statuses
from task_manager.statuses.forms import StatusForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class ListStatusesView(ListView):
    template_name = 'statuses/status_list.html'
    model = Statuses


class StatusesCreateView(SuccessMessageMixin, CreateView):
    template_name = 'statuses/status_create.html'
    model = Statuses
    form_class = StatusForm
    success_url = reverse_lazy('statuses:list_statuses')
    success_message = _('Status successfully created')


class StatusUpdateView(UpdateView):
    pass


class StatusDeleteView(DeleteView):
    pass
