from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_link, name = "main"),
    path("get-link", views.get_link, name = "get-link"),
    path("download", views.download, name = "download")
]