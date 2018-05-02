from django.shortcuts import render

from core.models import Projet, Membre


def core_home(request):
    """vue affichant la page d'acceuil, renvoie le queryset du projet phare"""
    projet_phare = Projet.objects.get(phare=True)
    chef = projet_phare.chef
    graphistes = projet_phare.graphiste.all()
    musiciens = projet_phare.musicien.all()
    scenaristes = projet_phare.scenariste.all()
    codeurs = projet_phare.codeur.all()
    return render(request, 'core/coreHome.html', locals())
