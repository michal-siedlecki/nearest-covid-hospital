from django.contrib.gis.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()
    address = models.CharField(max_length=200)
    phones = models.CharField(max_length=200)
    point_type = models.CharField(max_length=200)

    def phones_as_list(self):
        return self.phones.split(',')






