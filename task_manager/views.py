from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect


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


class Logout(LogoutView):
    def post(self, request, *args, **kwargs):
        auth_logout(request)
        messages.info(self.request, _('You are logged out'))
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)
