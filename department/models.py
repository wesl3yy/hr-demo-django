import uuid

from django.db import models


# Create your models here.
class Department(models.Model):
    id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=36)
    name = models.CharField(max_length=255)
    description = models.TextField()

    organization = models.ForeignKey('organization.Organization', on_delete=models.CASCADE)

    class Meta:
        db_table = 'departments'
