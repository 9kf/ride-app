from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
        ('EN-ROUTE', 'En-route'),
        ('PICKUP', 'Pickup'),
        ('DROPOFF', 'Dropoff'),
    )

class Ride(models.Model):
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_rider', related_query_name='rides_as_rider', default=None)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver', related_query_name='rides_as_driver', default=None)

    class Meta:
        db_table = 'ride'
    
class RideEvent(models.Model):
    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='event', related_query_name='event')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ride_event'
