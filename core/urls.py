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
from django.urls import path, include

from core import views
from core.models import Projet

import sys

urlpatterns = [
    path('', views.core_home, name='core_home'),
    # path('ezo', include('ezo.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

projets_liste = Projet.objects.all()
for projet in projets_liste:
    try:
        urlpatterns += path(str(projet.slug), include(str(projet.slug) + '.urls'))
    except:
        print("Unexpected error:", sys.exc_info()[0])
