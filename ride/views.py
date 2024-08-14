from rest_framework import permissions, viewsets
from .models import Ride, RideEvent
from .serializers import RideSerializer, RideEventSerializer

class RidesListViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    
class RideEventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer