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
    chef = models.OneToOneField('Membre', verbose_name="chef de projet",
                                  related_name="chef",null=True, blank=True, on_delete=models.PROTECT)
    graphiste = models.ManyToManyField('Membre', verbose_name="Graphiste(s)",
                                       related_name="graphiste", blank=True)
    musicien = models.ManyToManyField('Membre', verbose_name="Musicien(s)",
                                      related_name="musicien", blank=True)
    codeur = models.ManyToManyField('Membre', verbose_name="Codeur(s)",
                                    related_name="codeur", blank=True)
    etat = models.BooleanField(verbose_name="Terminé ?", default=False)
    phare = models.BooleanField(verbose_name="Projet Phare ?", default=False)

    def __str__(self):
        return self.nom


class Membre(models.Model):
    """class définissant les membres producteur de la communautée, rattaché ou non à
    des projets."""
    pseudo = models.CharField(max_length=100)

    def __str__(self):
        return self.pseudo
