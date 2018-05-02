from django.db import models
from django.utils import timezone

from markdownx.models import MarkdownxField


class Projet(models.Model):
    """class définissant chaque projet en cours, une description du projet,
    son header et son titre"""
    nom = models.CharField(max_length=100)
    slug = models.SlugField()
    description = MarkdownxField()
    header = models.ImageField(upload_to='projet/img/upload/')
    chef = models.ForeignKey('Membre', on_delete=models.PROTECT, null=True,
                             verbose_name="chef de projet")
    graphiste = models.ManyToManyField('Membre', verbose_name="Graphiste(s)",
                                       related_name="graphiste", blank=True)
    musicien = models.ManyToManyField('Membre', verbose_name="Musicien(s)",
                                      related_name="musicien", blank=True)
    scenariste = models.ManyToManyField('Membre', verbose_name="Scénariste(s)",
                                        related_name="scenariste", blank=True)
    codeur = models.ManyToManyField('Membre', verbose_name="Codeur(s)",
                                    related_name="codeur", blank=True)
    etat = models.BooleanField(verbose_name="Terminé ?", default=False)
    phare = models.BooleanField(verbose_name="Projet Phare ?", default=False)

    # tab customisation
    couleur_tab_texte = models.CharField(max_length=7, default="#d500f9", blank=True)
    couleur_tab_active_background = models.CharField(max_length=7, default="#f3e5f5", blank=True)
    couleur_tab_soulignement = models.CharField(max_length=7, default="#4a148c", blank=True)

    def __str__(self):
        return self.nom


class Membre(models.Model):
    """class définissant les membres producteur de la communautée, rattaché ou non à
    des projets."""
    pseudo = models.CharField(max_length=100)

    def __str__(self):
        return self.pseudo
