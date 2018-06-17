from django.contrib.gis import admin
<<<<<<< HEAD
from .models import Unit, counties,User_prof
=======
from .models import Unit, counties,WordBorder
>>>>>>> 8214f55aaf0a604ff0261cf0738e0a95cc72d92c
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
# class UnitAdmin(admin.ModelAdmin):
#     list_display = ('name','location')

admin.site.register(Unit, LeafletGeoAdmin)
admin.site.register(counties, LeafletGeoAdmin)
<<<<<<< HEAD
admin.site.register(User_prof)
=======
admin.site.register(WordBorder, LeafletGeoAdmin)
>>>>>>> 8214f55aaf0a604ff0261cf0738e0a95cc72d92c
