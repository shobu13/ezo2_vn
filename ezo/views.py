from django.shortcuts import render

from core.models import Projet


def ezo_home(request):
    return render(request, 'ezo/ezoHome.html', locals())
