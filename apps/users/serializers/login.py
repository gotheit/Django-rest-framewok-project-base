"""Serializer login."""
# django
from django.utils import timezone
# django rest framework
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginGetTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer that verifies and generates the access token for users."""
    @classmethod
    def get_token(cls, user):
        """Valid and generates access token."""
        token = super().get_token(user)
        """if not user.is_verified:
            raise serializers.ValidationError(
                {
                    "user": ['UNVERIFIED_USER']
                }
            )"""
        return token

    def validate(self, attrs):
        """Validates and obtains authentication and refresh token.
        also sends the last time and date of authentication.
        """
        data = super().validate(attrs)
        user = self.user
        refresh = self.get_token(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['last_login'] = {}
        if user.last_login is not None:
            data['last_login']['date'] = user.last_login.strftime("%d-%m-%Y")
            data['last_login']['hour'] = user.last_login.strftime("%H:%M:%S")
        else:
            data['last_login'] = None
        user.last_login = timezone.now()
        user.save()
        return data
