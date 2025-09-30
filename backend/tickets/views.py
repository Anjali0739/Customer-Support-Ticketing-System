from rest_framework import viewsets, permissions
from .models import Ticket
from .serializers import TicketSerializer


# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
