from django.urls import path
from . import views

urlpatterns = [
    path('', views.archive_list, name='archive_list'),
]
