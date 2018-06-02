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
        
