from django.urls import path
from task_manager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TasksListVew.as_view(), name='list_tasks'),
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path(
        '<int:pk>/update/',
        views.TaskUpdateView.as_view(),
        name='update_task'
    ),
    path(
        '<int:pk>/delete/',
        views.TaskDeleteView.as_view(),
        name='delete_task'
    ),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail_task'),
]
