from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("live-checker/", views.live_checker, name="live_checker"),
    path("about-us/", views.about_us, name="about_us"),
    path("resources/", views.resources, name="resources"),
]