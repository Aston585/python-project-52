from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class HomePageView(TemplateView):
    template_name = "index.html"


class Login(LoginView):
    pass


class Logout(LogoutView):
    pass
