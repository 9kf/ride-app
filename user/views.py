from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import permissions

class ProfilesView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Profile.objects.all();
    serializer_class = ProfileSerializer
