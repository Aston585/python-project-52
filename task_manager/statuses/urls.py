from django.urls import path
from task_manager.statuses import views

app_name = "statuses"

urlpatterns = [
    path('', views.ListStatusesView.as_view(), name='list_statuses'),
    path('create/', views.StatusesCreateView.as_view(), name='create_status'),
    path(
        '<int:pk>/update/',
        views.StatusUpdateView.as_view(),
        name='update_status',
    ),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(),
         name='delete_status'),
]
