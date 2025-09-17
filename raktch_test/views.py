from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

import requests
import json

from .serializers import RegisterSerializer, MyTokenObtainPairSerializer


API_BASE = "http://127.0.0.1:8000/api/auth/"

#####----- API VIEWS -----#####
# Signup (register)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# Logout API (blacklist refresh token)
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            raise ParseError("Refresh token required")

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logged out"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#####----- TEMPLATE VIEWS -----#####
# Signup page
class SignupPage(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        data = {
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
            "password2": request.POST.get("password2"),
        }
        r = requests.post(
            API_BASE + "signup/",
            data=json.dumps(data),
            headers={"Content-Type": "application/json"}
        )
        if r.status_code == 201:
            return redirect("login_page")
        return render(request, "register.html", {"error": r.json()})
    

class LogoutRedirect(View):
    def post(self, request):
        request.session.flush()
        return redirect("login_page")


# Login page
class LoginPage(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Use authenticate + JWT directly instead of serializer
        user = authenticate(username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            request.session['access'] = str(refresh.access_token)
            request.session['refresh'] = str(refresh)
            request.session['user_email'] = email
            return redirect("dashboard_page")
        
        
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

# Dashboard page
class DashboardPage(View):
    def get(self, request):
        access_token = request.session.get("access")
        if not access_token:
            return redirect("login_page")
        user_email = request.session.get("user_email", "User")
        return render(request, "dashboard.html", {"user_email": user_email})
