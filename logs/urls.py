from django.urls import path
from .views import LogListView, ClearLogsView

urlpatterns = [
    path('', LogListView.as_view(), name='log-list'),
    path('clear/', ClearLogsView.as_view(), name='log-clear'),
]