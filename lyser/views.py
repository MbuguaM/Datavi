from django.shortcuts import render
from .models import counties
from django.core.serializers import serialize
from django.http import HttpResponse
from . import views

# Create your views here.
def landing(request):
    """ models displaying the main landing page """
    return render (request, 'app_temp/home.html')


def county_data(request):
    """ fetching the county data """
    county = serialize('geojson',counties.objects.all())

    return render(county, content_type = 'json')



def more_about(request):
    """ displaying more inforamtion about us """
    return render(request, 'app_temp/us.html')

def projection(request):
    """displaying map projection"""
    return render(request, 'app_temp/projection.html')
