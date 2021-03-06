from django.urls import path,re_path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', views.landing, name = 'landing'),
    re_path(r'^more_about$',views.more_about, name='more_about'),
    re_path(r'^projection$',views.projection, name='projection'),
    re_path(r'^your_projection$', views.your_projection, name='your_projection'),
    re_path(r'^documentation$',views.documentation,name = 'documentation'),
    re_path(r'^stories$',views.stories,name = 'stories'),

    # loading infomation as json 
    re_path(r'^county_data$',views.county_data, name = 'county_data' ),
    re_path(r'^world_borders$', views.world_borders, name = 'world_borders'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
