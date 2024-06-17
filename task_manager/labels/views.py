from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import LoginRequiredCustomMixin
from django.contrib import messages
from django.shortcuts import redirect


class LabelsListView(
    LoginRequiredCustomMixin,
    ListView,
):
    template_name = 'labels/labels_list.html'
    model = Label


class LabelCreateView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    CreateView,
):
    template_name = 'labels/label_create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:list_labels')
    success_message = _('Label successfully created')


class LabelUpdateView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = 'labels/label_update.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:list_labels')
    success_message = _('Label successfully changed')


class LabelDeleteView(
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = 'labels/label_delete.html'
    model = Label
    success_url = reverse_lazy('labels:list_labels')
    success_message = _('Label successfully deleted')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.tasks_with_this_label.exists():
            messages.error(
                request,
                _('Cannot delete label because it is in use')
            )
            return redirect(self.success_url)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
