from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class HomePageView(TemplateView):
    template_name = "index.html"


class Login(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        messages.success(self.request, _('Login successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Login Error'))
        return super().form_invalid(form)


class LogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)

