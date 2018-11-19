"""core URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.shortcuts import render

from ezo import views

urlpatterns = [
    path('', views.ezo_home, name='ezo_home'),
    path('galerie', views.ezo_galerie, name='ezo_galerie'),
    path('histoire', views.ezo_histoire, name='ezo_histoire'),
    path('info', views.ezo_info, name='ezo_info'),
    path('personnages', views.ezo_personnages, name='ezo_personnages'),
    path('personnages/<slug:perso>', views.ezo_personnages, name='ezo_personnages'),
    path('special', views.ezo_special, name='ezo_special'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
