from .forms import UserCreate
from django.contrib.auth.views import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.utils.translation import gettext_lazy as _
# from django.contrib.messages.views import SuccessMessageMixin


class ListUsers(ListView):
    model = get_user_model()
    template_name = "users/users_list.html"


class UserCreate(CreateView):
    form_class = UserCreate
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('home')


class UserEdit(UpdateView):
    pass


class UserDelete(DeleteView):
    pass
