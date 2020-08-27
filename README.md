# Nearest COVID-19 hospital finder

Application finds COVID-19 hospital closest to You based on Your geolocation. Database covers hospitals in Poland.

![sample](/img/vid.gif)
---
### Demo app is hosted on Heroku
![LINK](https://szpitale-covid.herokuapp.com/)

## Getting Started

$ git clone https://github.com/michal-siedlecki/nearest-covid-hospital

### Prerequisites

What things you need to install the software:

1. Python 3+
2. Django 3.0.4
3. PostgreSQL database
4. PostGIS extension for supporting spatial features in the PostgreSQL database
6. Docker for installing PostgreSQL and PostGIS

### Installing

1. Install GeoDjango Dependencies (GEOS, GDAL, and PROJ.4)
2. Setup spatial Database with PostgreSQL and PostGIS engine in docker container: 
```
$ docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```
3. Create virtual enviroment
4. Navigate to nearest_covid_hospital/nearest_hospital app and run django
```
python manage.py runserver
```

## Built With

* The Python programming language
* The Django web framework
* The PostgreSQL database
* The PostGIS extension
* Pip for installing dependencies
* The venv module
* Docker

## Authors

* **Michał Siedlecki**
