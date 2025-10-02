from django.db import models
from location.models import Location


class LocationService:
    @staticmethod
    def search_location(keyword):
        return Location.objects.filter(
            models.Q(name__icontains=keyword) |
            models.Q(address__icontains=keyword) |
            models.Q(city__icontains=keyword)
        )