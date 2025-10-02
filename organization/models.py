import uuid

from django.db import models

# Create your models here.
class Organization(models.Model):
    id = models.CharField(primary_key=True, default=str(uuid.uuid4()), max_length=36)
    name = models.CharField(max_length=255)
    description = models.TextField()
    config = models.JSONField()

    class Meta:
        db_table = 'organizations'
