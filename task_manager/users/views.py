from task_manager.users.forms import UserCreateForm
from django.contrib.auth.models import User as UserModel
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class ListUsersView(ListView):
    model = UserModel
    template_name = "users/users_list.html"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('home')
    success_message = _('User successfully registered')


class UserEditView(SuccessMessageMixin, UpdateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy("users:list_users")
    success_message = _("User successfully changed")
    failure_message = _("You do not have permission to change another user.")
    failure_url = reverse_lazy("users:list_users")


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = UserModel
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("users:list_users")
    success_message = _('User deleted successfully')
    failure_message = _("You do not have permission to change another user.")
    failure_url = reverse_lazy('users:list_users')
