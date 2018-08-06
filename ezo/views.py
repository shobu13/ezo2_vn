from django.shortcuts import render

from core.models import Projet


def ezo_home(request):
    return render(request, 'ezo/index.html', locals())


def ezo_galerie(request):
    return render(request, 'ezo/galerie.html', locals())


def ezo_histoire(request):
    return render(request, 'ezo/histoire.html', locals())


def ezo_info(request):
    return render(request, 'ezo/info.html', locals())


def ezo_personnages(request):
    return render(request, 'ezo/personnages.html', locals())


def ezo_special(request):
    return render(request, 'ezo/special.html', locals())
