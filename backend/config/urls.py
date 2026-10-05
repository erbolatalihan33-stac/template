from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView
from api.views import ProfileView
urlpatterns = [
    path("api/profile", vip.profile),
    path("api/book", vip.book),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),

    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/profile/", ProfileView.as_view()),

]
