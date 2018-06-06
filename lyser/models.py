from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager

# Create your models here
class Unit(models.Model):
    """ model that saves unit data on a project """
    name = models.CharField(max_length = 20)
    location = gis_models.PointField(srid = 4326)
    objects = GeoManager()

    def __str__(self):
        return self.name

class counties(models.Model):
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom =gis_models.MultiPolygonField(srid=4326)
        
    def __str__(self):
        return self.county