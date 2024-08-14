import datetime
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import permissions, viewsets
from django.contrib.auth.models import User
from .models import Ride, RideEvent, STATUS_CHOICES
from .serializers import RideSerializer, RideEventSerializer

class RidesListViewset(viewsets.ViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Ride.objects.all()

    def list(self, request):
        ride_status = request.query_params.get('status')
        rider_email = request.query_params.get('rider-email')

        filtered_queryset = self.queryset

        if ride_status is not None:
            if ride_status in dict(STATUS_CHOICES):
                filtered_queryset = filtered_queryset.filter(status=ride_status)
            else:
                raise Exception("Invalid ride status")

        if rider_email is not None:
            user = User.objects.filter(email=rider_email).first()
            if user is not None:
                filtered_queryset = filtered_queryset.filter(rider=user)
            else:
                raise Exception('Invalid user')

        ride_events = RideEvent.objects.filter(id_ride=self.queryset.first().pk, created_at__gt=datetime.date.today() - datetime.timedelta(days=1))

        ride_serialzer = RideSerializer(filtered_queryset, many=True)
        events_serializer = RideEventSerializer(ride_events, many=True)

        return Response({"rides": ride_serialzer.data, "todays_ride_events": events_serializer.data})
    
class RideEventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer