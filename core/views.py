from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, reverse

from core.models import Projet, Config


def core_home(request):
    """vue affichant la page d'acceuil, renvoie le queryset du projet phare"""
    projet_phare = Projet.objects.get(phare=True)
    chef = projet_phare.chef
    graphistes = projet_phare.graphiste.all()
    musiciens = projet_phare.musicien.all()
    scenaristes = projet_phare.scenariste.all()
    codeurs = projet_phare.codeur.all()

    # récupération des projets et tri
    projets_term_liste = Projet.objects.filter(etat=True)
    projets_progress_liste = Projet.objects.filter(etat=False)

    #récupération a_propos
    a_propos = Config.objects.get(enable=True).a_propos

    return render(request, 'core/coreHome.html', locals())


