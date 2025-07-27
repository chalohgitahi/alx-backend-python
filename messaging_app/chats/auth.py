from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer

# We move the User Registration View here from views.py
class UserRegisterView(generics.CreateAPIView):
    """
    View for new users to register.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # We allow any user (even unauthenticated ones) to access this endpoint.
    permission_classes = [permissions.AllowAny]