import uuid

from django.db import models


# Create your models here.
class Employee(models.Model):
    id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=36)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    class Meta:
        db_table = 'employees'
