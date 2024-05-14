from django.urls import path
from task_manager.users import views

app_name = "users"

urlpatterns = [
    path('', views.ListUsersView.as_view(), name='list_users'),
    path('create/', views.UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/update/', views.UserEditView.as_view(), name='edit_user'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(),
         name='delete_user'),
]
