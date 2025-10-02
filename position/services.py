from django.db import models
from position.models import Position


class PositionService:
    @staticmethod
    def search_position(keyword):
        return Position.objects.filter(
            models.Q(name__icontains=keyword)
        )