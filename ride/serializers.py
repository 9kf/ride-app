from rest_framework import serializers
from .models import Ride, RideEvent
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id', 'username', 'first_name', 'last_name', 'email']

class RideSerializer(serializers.ModelSerializer):
    rider = serializers.SerializerMethodField()
    driver = serializers.SerializerMethodField()
    class Meta:
        model = Ride
        fields = ['id', 'status', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude', 'pickup_time', 'rider', 'driver']

    def get_rider(self, obj):
        return UserSerializer(obj.rider).data
    
    def get_driver(self, obj):
        return UserSerializer(obj.driver).data

class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = '__all__'
    
    def __str__(self):
        return str(self.title)


    