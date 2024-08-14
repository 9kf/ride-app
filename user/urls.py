from django.urls import path
from . import views

from . import views

urlpatterns = [
    path("profiles/", views.ProfilesView.as_view(), name="profile-list-create-view"),
]