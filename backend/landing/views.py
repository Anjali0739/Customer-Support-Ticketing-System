from django.shortcuts import render

# Create your views here.


def home(request):
    endpoints = [
        {"name": "Login / Get JWT Token", "method": "POST", "url": "/api/auth/token/"},
        {"name": "Refresh Token", "method": "POST", "url": "/api/auth/token/refresh/"},
        {"name": "Get Profile", "method": "GET", "url": "/api/auth/me/"},
        {"name": "List Tickets", "method": "GET", "url": "/api/tickets/"},
        {"name": "Create Ticket", "method": "POST", "url": "/api/tickets/"},
        {"name": "Ticket Detail", "method": "GET", "url": "/api/tickets/<id>/"},
    ]
    return render(request, "landing/index.html", {"endpoints": endpoints})
