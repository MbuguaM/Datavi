from django.shortcuts import render
from .models import counties, WordBorder
from django.core.serializers import serialize
from django.http import HttpResponse
from . import views

# Create your views here.
def landing(request):
    """ models displaying the main landing page """
    return render (request, 'app_temp/home.html')

def more_about(request):
    """ displaying more inforamtion about us """
    return render(request, 'app_temp/us.html')

def projection(request):
    """displaying map projection"""
    return render(request, 'app_temp/projection.html')

def documentation(request):
    """displaying detailed map infomation"""
    return render(request, 'app_temp/Documentation.html')


# Provider urls ( urls for providing geometric data)
def county_data(request):
    """ fetching the county data """
    county = serialize('geojson',counties.objects.all())
    return HttpResponse(county, content_type = 'json')

def world_borders(request):
    """ fetching the world borders data"""
    world_borders = serialize('geojson',WordBorder.objects.all())
    return HttpResponse(world_borders, content_type = 'json')