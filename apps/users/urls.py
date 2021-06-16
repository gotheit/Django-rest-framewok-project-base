"""Users urls."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views

from apps.users.views import LoginGetTokenObtainPairView

# Wire up our API using automatic URL routing.

# Additionally, we include login URLs for the browsable API.
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # POST
    path('token/', LoginGetTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # POST
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    # POST
    path('token/verify/', views.TokenVerifyView.as_view(), name='token_verify'),
    ]
