from django.urls import path,re_path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', views.landing, name = 'landing'), 
    re_path(r'^county_data$',views.county_data, name = 'county_data' ), 
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
