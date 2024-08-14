import datetime
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .models import Ride, RideEvent, STATUS_CHOICES
from .serializers import RideSerializer, RideEventSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RidesListViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    
class RideEventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer