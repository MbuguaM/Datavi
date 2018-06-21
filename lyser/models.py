from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here


class Unit(models.Model):
    """ model that saves unit data on a project """
    name = models.CharField(max_length=20)
    location = gis_models.PointField(srid=4326)
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
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.county


class User_prof(models.Model):
    """ model that hold infomation on the user """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    mail_confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    def delete(self):
        """ redifining the mail_confirm field in the user_prof"""
        self.mail_confirm = False
        self.save()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        User_prof.objects.create(user=instance)
    instance.profile.save()


class WordBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name
