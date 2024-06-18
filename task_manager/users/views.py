from task_manager.users.forms import UserCreation
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    LoginRequiredCustomMixin,
    UserPassesTestCustomMixin,
    DeleteProtectionMixin,
)


class ListUsersView(ListView):
    model = get_user_model()
    template_name = "users/users_list.html"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = UserCreation
    template_name = 'form_create_update.html'
    success_url = reverse_lazy('login')
    success_message = _('User successfully registered')
    extra_context = {
        'header': _('Registration'),
        'button': _('Register'),
    }


class UserUpdateView(
    UserPassesTestCustomMixin,
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = get_user_model()
    form_class = UserCreation
    template_name = 'form_create_update.html'
    success_url = reverse_lazy('users:list_users')
    success_message = _('User successfully changed')
    failure_message = _('You do not have permission to change another user.')
    extra_context = {
        'header': _('Changing User'),
        'button': _('Change'),
    }


class UserDeleteView(
    UserPassesTestCustomMixin,
    LoginRequiredCustomMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = get_user_model()
    template_name = 'form_delete.html'
    success_url = reverse_lazy('users:list_users')
    success_message = _('User deleted successfully')
    protected_url = reverse_lazy('users:list_users')
    protected_message = _('Cannot delete user because it is in use')
    extra_context = {
        'header': _('Remove user'),
    }
