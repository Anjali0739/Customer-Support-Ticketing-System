from .models import Ticket
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json
from django.http import JsonResponse



# Create your views here.
@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def create_view_ticket(request):
    user = request.user

    if request.method=="POST":
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        
        if not title or not description:
            return JsonResponse({"error":"both title and description are required"}, status=400)
        
        ticket = Ticket.objects.create(title=title, description=description, user_id=user)
        return JsonResponse({"message":"Ticket created successfully!", "Ticket_id":ticket.id, "User":user.username}, status=201)
    


    elif request.method=="GET":
        ticket = Ticket.objects.all().order_by('-last_updated_at')
        data = [{
            "id":t.id,
            "title":t.title,
            "description":t.description,
            "created_at":t.created_at
        } for t in ticket]

        return JsonResponse({"User":user.username,"tickets":data}, status=200)





@api_view(["GET","PUT", "Delete"])
@permission_classes([IsAuthenticated])
def view_update_delete(request, id):
    user = request.user

    ticket=Ticket.objects.filter(id=id, user_id=user).first()

    if ticket is None:
        return JsonResponse({"error":"ticket not found"}, status=400)

    if request.method=="GET":
        return JsonResponse({
            "id":ticket.id,
            "title":ticket.title,
            "description":ticket.description,
            "created_at":ticket.created_at
        }, status=200)
    

    elif request.method=="PUT":
        data = json.loads(request.body)
        
        ticket.title = data.get('title', ticket.title)
        ticket.description = data.get('description', ticket.description)
        ticket.save()

        return JsonResponse({"message":"ticket updated successfully!", "ticket_id":ticket.id}, status=200)
    


    elif request.method=="DELETE":
        ticket.delete()
        return JsonResponse({"message":"ticket deleted successfully!", "ticket_id":id}, status=200)



