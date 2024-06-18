from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class HomePageView(TemplateView):
    template_name = "index.html"


class Login(
    SuccessMessageMixin,
    LoginView,
):
    template_name = "login.html"
    success_message = _('Login successfully')
    failure_message = _('Please enter the correct username and password.'
                        'Both fields can be case sensitive.')

    def form_invalid(self, form):
        messages.error(self.request, self.failure_message)
        return super().form_invalid(form)


class Logout(
    SuccessMessageMixin,
    LogoutView,
):
    success_message = _('You are logged out')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
