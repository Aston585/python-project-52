from task_manager.users.forms import UserCreateForm
from django.contrib.auth.views import get_user_model
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from django.utils.translation import gettext_lazy as _
# from django.contrib.messages.views import SuccessMessageMixin


class ListUsersView(ListView):
    model = get_user_model()
    template_name = "users/users_list.html"


class UserCreateView(CreateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('home')


class UserEditView(UpdateView):
    pass


class UserDeleteView(DeleteView):
    pass
