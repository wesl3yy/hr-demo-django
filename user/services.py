from django.db import models
from user.models import UserProfile


class UserService:
    @staticmethod
    def search(
        keyword="",
        locations_ids=None,
        organization_ids=None,
        department_ids=None,
        position_ids=None
    ):
        qs = UserProfile.objects.filter(status=True)

        if keyword:
            qs = qs.filter(
                models.Q(first_name__icontains=keyword) |
                models.Q(last_name__icontains=keyword) |
                models.Q(email__icontains=keyword)
            )

        if locations_ids:
            qs = qs.filter(location_id__in=locations_ids)
        if organization_ids:
            qs = qs.filter(organization_id__in=organization_ids)
        if department_ids:
            qs = qs.filter(department_id__in=department_ids)
        if position_ids:
            qs = qs.filter(position_id__in=position_ids)

        return qs
