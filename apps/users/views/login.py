"""Views login."""
from rest_framework_simplejwt.views import TokenObtainPairView

# serializers
from apps.users.serializers import LoginGetTokenObtainPairSerializer


class LoginGetTokenObtainPairView(TokenObtainPairView):
    """Custom TokenObtainPairView of rest_framework_simplejwt."""
    serializer_class = LoginGetTokenObtainPairSerializer
