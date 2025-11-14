from django.urls import path
from .views import create_view_ticket

urlpatterns = [
    path("", create_view_ticket, name="create_view_ticket"),
]
