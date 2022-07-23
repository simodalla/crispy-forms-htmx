from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("check-username", views.check_username, name="check-username"),
    path("check-subject", views.check_subject, name="check-subject"),
]
