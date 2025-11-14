from django.urls import path
from .views import create_view_ticket, view_update_delete

urlpatterns = [
    path("", create_view_ticket, name="create_view_ticket"),
    path("<int:id>/", view_update_delete, name="view_update_delete"),
]
