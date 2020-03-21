from django.urls import path
from . import views

urlpatterns = [
    # [...]

    path('hospitals/<lat>/<lon>', views.hospital_list, name='hospitals'),
    path('hospitals', views.home, name='hospitals'),
    path('', views.home, name='home')

]
