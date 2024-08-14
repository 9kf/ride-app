from rest_framework import serializers
from .models import Ride, RideEvent
from django.contrib.auth.models import User
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id', 'username', 'first_name', 'last_name', 'email']

class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = '__all__'

class RideSerializer(serializers.ModelSerializer):
    rider_lookup = serializers.SerializerMethodField()
    driver_lookup = serializers.SerializerMethodField()
    todays_ride_events = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = ['id', 'status', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude', 'pickup_time', 'rider', 'driver', 'todays_ride_events', 'rider_lookup', 'driver_lookup']

    def get_rider_lookup(self, obj):
        return UserSerializer(obj.rider).data
    
    def get_driver_lookup(self, obj):
        return UserSerializer(obj.driver).data

    def get_todays_ride_events(self,obj):
        ride_events = RideEvent.objects.filter(id_ride=obj.id,created_at__gt=datetime.date.today() - datetime.timedelta(days=1))
        events_serializer = RideEventSerializer(ride_events, many=True)
        return events_serializer.data


    