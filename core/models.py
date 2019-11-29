from django.db import models

# Create your models here.
class Place(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    estimated_date = models.DateField()