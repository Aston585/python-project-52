from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Statuses


class ListStatusesView(ListView):
    template_name = 'statuses/status_list.html'
    model = Statuses


class StatusesCreateView(CreateView):
    pass


class StatusUpdateView(UpdateView):
    pass


class StatusDeleteView(DeleteView):
    pass
