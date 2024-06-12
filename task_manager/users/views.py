from task_manager.users.forms import UserCreateForm
from django.contrib.auth import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import (
    LoginRequiredCustomMixin,
    UserPassesTestCustomMixin,
)
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError


class ListUsersView(ListView):
    model = get_user_model()
    template_name = "users/users_list.html"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('login')
    success_message = _('User successfully registered')


class UserUpdateView(
    UserPassesTestCustomMixin,
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = 'users/update_user.html'
    success_url = reverse_lazy('users:list_users')
    success_message = _('User successfully changed')
    failure_message = _('You do not have permission to change another user.')


class UserDeleteView(
    UserPassesTestCustomMixin,
    LoginRequiredCustomMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = get_user_model()
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('users:list_users')
    success_message = _('User deleted successfully')
    failure_message = _('Cannot delete user because it is in use')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, self.failure_message)
            return redirect(request.META.get('HTTP_REFERER', self.success_url))
