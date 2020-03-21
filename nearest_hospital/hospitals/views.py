from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Hospital


def hospital_list(request, lat=0, lon=0):
    lat = float(lat)
    lon = float(lon)
    user_location = Point(lon, lat, srid=4326)
    context = dict()
    context['hospitals'] = Hospital.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[:4]
    return render(request, 'hospitals/hospitals.html', context)


def home(request):
    return render(request, template_name='hospitals/index.html')
