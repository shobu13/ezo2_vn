from django.shortcuts import render


def core_home(request):
    """vue affichant la page d'acceuil, renvoie le queryset du projet phare"""
    return render(request, 'core/coreHome.html')
