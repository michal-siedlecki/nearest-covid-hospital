from django.contrib.gis.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)


