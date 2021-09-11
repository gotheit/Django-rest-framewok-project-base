"""Views login."""
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

# serializers
from apps.users.serializers import LoginGetTokenObtainPairSerializer


class LoginGetTokenObtainPairView(TokenObtainPairView):
    """Custom TokenObtainPairView of rest_framework_simplejwt."""
    serializer_class = LoginGetTokenObtainPairSerializer


def home(request):
    """Home page."""
    return render(request, "home/index.html")