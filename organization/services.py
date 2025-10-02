from django.db import models
from organization.models import Organization


class OrganizationService:
    @staticmethod
    def search_organizations(keyword):
        return Organization.objects.filter(
            models.Q(name__icontains=keyword) |
            models.Q(description__icontains=keyword)
        )
