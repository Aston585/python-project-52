from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class LoginRequiredCustomMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                self.request,
                _('You are not authorized! Please log in.'),
            )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class UserPassesTestCustomMixin:

    def get_object(self):
        return get_user_model().objects.get(pk=self.kwargs.get("pk"))

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id

    def dispatch(self, request, *args, **kwargs):

        if not self.test_func():
            messages.error(
                self.request,
                _('You do not have permission to change another user.'),
            )
            return redirect('users:list_users')
        return super().dispatch(request, *args, **kwargs)
