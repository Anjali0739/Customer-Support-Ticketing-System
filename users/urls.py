from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserProfileView
from django.http import JsonResponse



def auth_home(request):
    return JsonResponse({
        "message": "Auth Endpoints",
        "get_token": "/api/auth/token/",
        "refresh_token": "/api/auth/token/refresh/",
        "current_user_profile": "/api/auth/me/"
    })




urlpatterns = [
    path("", auth_home),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", UserProfileView.as_view(), name="user_profile"),
]

