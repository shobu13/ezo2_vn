from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, reverse

from core.models import Projet


def core_home(request):
    """vue affichant la page d'acceuil, renvoie le queryset du projet phare"""
    projet_phare = Projet.objects.get(phare=True)
    chef = projet_phare.chef
    graphistes = projet_phare.graphiste.all()
    musiciens = projet_phare.musicien.all()
    scenaristes = projet_phare.scenariste.all()
    codeurs = projet_phare.codeur.all()

    # récupération des projets et tri
    projets_raw = Projet.objects.all()
    projets_liste = []

    for i in range(0, len(projets_raw), 2):
        projets_liste += (projets_raw[i:i + 2],)

    return render(request, 'core/coreHome.html', locals())


