from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

# Create your views here.




@csrf_exempt
def register_user(request):
    if request.method=="POST":
        try:
            user_data = json.loads(request.body)
            username = user_data.get('username')
            email = user_data.get('email')
            password = user_data.get('password')

            if not username or not email or not password:
                return JsonResponse({"error":"username, email, and password are required"}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error":"email already registered"}, status=400)
            
            User.objects.create_user(username=username, email=email, password=password)
            return JsonResponse({"message":"User registered successfully"}, status=201)
        
        except:
            return JsonResponse({"error":"Invalid JSON format"}, status=400)
        
    else:
        return JsonResponse({"error":"Invalid HTTP method used"}, status=405)
    


@csrf_exempt
def login_user(request):
    if request.method=="POST":
        try:
            user_data = json.loads(request.body)
            username = user_data.get("username")
            password = user_data.get("password")

            if not username or not password:
                return JsonResponse({"error":"both username and password are required"}, status=400)
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    "message": "user logged in successfully!",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token)
                }, status=200)
            else:
                return JsonResponse({"error": "Invalid username or password"}, status=401)

        except:
            return JsonResponse({"error":"Invalid JSON format"}, status=400)
        
    else:
        return JsonResponse({"error":"Invalid HTTP method used"}, status=405)
    


