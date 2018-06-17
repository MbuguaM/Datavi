"""Datavi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.gis import admin
from django.urls import path, include, re_path
from django.contrib.auth import views
from lyser import views as auth_views
from lyser.forms import LoginForm



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lyser.urls')),
    # entry and exit control urls
    re_path(r'^accounts/login/$', views.LoginView.as_view(template_name = 'registration/login.html', authentication_form = LoginForm,), name='login'),
    re_path(r'^signup/$', auth_views.signup, name='signup'),
    re_path(r'^logout/$', views.logout, {'next_page': 'login'}, name='logout'),
    # mail confimation urls
    re_path(r'^account_activation_sent/$', auth_views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.activate, name='activate'),
]
