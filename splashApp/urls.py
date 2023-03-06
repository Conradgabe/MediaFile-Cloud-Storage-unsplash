from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("", views.all_images, name="all-images"),
    path("uploaded/", views.uploaded, name="uploaded"),
    path("search/", views.search, name="search")
]