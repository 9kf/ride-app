from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', views.RidesListViewset, basename='rides')
router.register(r'events', views.RideEventViewSet, basename='ride-events')



urlpatterns = [
    path("", include(router.urls)),
]