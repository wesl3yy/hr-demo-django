import uuid

from django.db import models


# Create your models here.
class UserProfile(models.Model):
    id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=36)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=120)
    status = models.BooleanField(default=True)

    organization = models.ForeignKey('organization.Organization', on_delete=models.CASCADE)
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)
    position = models.ForeignKey('position.Position', on_delete=models.CASCADE)
    manager = models.ForeignKey('employee.Employee', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'users'
