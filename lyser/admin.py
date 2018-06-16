from django.contrib.gis import admin
from .models import Unit, counties,WordBorder
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
# class UnitAdmin(admin.ModelAdmin):
#     list_display = ('name','location')

admin.site.register(Unit, LeafletGeoAdmin)
admin.site.register(counties, LeafletGeoAdmin)
admin.site.register(WordBorder, LeafletGeoAdmin)