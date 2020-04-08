from django.db import migrations
import json
from django.contrib.gis.geos import fromstr


def load_data(apps, schema_editor):
    Hospital = apps.get_model('hospitals', 'Hospital')
    jsonfile = 'places.json'

    with open(str(jsonfile)) as datafile:
        data = json.load(datafile)

        for k, v in data.items():
            name = v.get('name')
            lon = float(v.get('lon'))
            lat = float(v.get('lat'))
            location = fromstr(f'POINT({lon} {lat})', srid=4326)
            address = v.get('address')
            phones = v.get('phone')
            point_type = v.get('point_type')
            Hospital(name=name, location=location, address=address, phones=phones, point_type=point_type).save()


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
