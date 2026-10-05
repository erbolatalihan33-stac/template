from django.urls import path

from .views import BookView, HealthView, ProfileView

urlpatterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile", ProfileView.as_view()),
    path("book/", BookView.as_view(), name="book"),
    path("book", BookView.as_view()),
]
