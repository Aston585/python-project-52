from django.urls import path
from task_manager.users import views

app_name = "users"

urlpatterns = [
    path('', views.ListUsers.as_view(), name='list_users'),
    path('create/', views.UserCreate.as_view(), name='create_user'),
    path('<int:pk>/update/', views.UserEdit.as_view(), name='edit_user'),
    path('<int:pk>/delete/', views.UserDelete.as_view(), name='delete_user'),
]
