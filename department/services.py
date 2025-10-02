from django.db import models
from department.models import Department


class DepartmentService:
    @staticmethod
    def search_departments(keyword):
        return Department.objects.filter(
            models.Q(name__icontains=keyword) |
            models.Q(description__icontains=keyword)
        )
