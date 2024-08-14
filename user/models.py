from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_ROLES = (
        ('ADMIN', 'Admin'),
        ('DRIVER', 'Driver'),
        ('RIDER', 'Rider'),
    )
    role = models.CharField(choices=USER_ROLES, max_length=10)
    phone_number = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, related_name="profile", related_query_name="profile", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
