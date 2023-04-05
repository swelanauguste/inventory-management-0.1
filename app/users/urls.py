from django.urls import path

from .views import ProfileUpdateView, profile_redirect

urlpatterns = [
    path("profile/<slug:slug>", ProfileUpdateView.as_view(), name="profile"),
    path("account/", profile_redirect, name="profile-redirect"),
]
