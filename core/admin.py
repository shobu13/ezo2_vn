from django.contrib import admin
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Projet, Membre

import os
import shutil


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'etat', 'app_is_create')
    list_filter = ('etat', 'phare')
    search_fields = ('nom',)
    ordering = ('nom',)
    prepopulated_fields = {'slug': ('nom',), }
    fieldsets = (
        ('Informations Générales', {
            # définis les champs qui y sont représenter
            'fields': ('nom', 'slug', 'description', 'header')
        }),
        ('App', {
            # définis les champs qui y sont représenter
            'fields': ('app_name', 'app_is_create')
        }),
        ('Membres', {
            # définis les champs qui y sont représenter
            'fields': ('chef', 'graphiste', 'musicien', 'scenariste', 'codeur')
        }),
        ('Customisation tabs', {
            'description': '<a href="http://materializecss.com/color.html#palette"  onclick="window.open(this.href); return false;">palette de couleur</a>',
            'classes': ('collapse',),
            'fields': (
                'couleur_tab_texte', 'couleur_tab_active_background', 'couleur_tab_soulignement')
        }),
        ('Autre', {
            # définis les champs qui y sont représenter
            'fields': ('etat', 'phare', 'adulte', )
        }),

    )

    actions = ['app_create', 'app_check', 'app_supr']

    def app_create(self, request, queryset):
        for item in queryset:
            if item.app_name in os.listdir():
                item.app_is_create = True
                item.save()
            else:
                try:
                    call_command('startapp', item.app_name)
                    item.app_is_create = True
                    item.save()
                except:
                    self.message_user(request,
                                      "une erreur est survenue, peut être que le nom de l'app est erroner.")

    def app_check(self, request, queryset):
        for item in queryset:
            if item.app_name in os.listdir():
                item.app_is_create = True
                item.save()
            else:
                item.app_is_create = False
                item.save()

    def app_supr(self, request, queryset):
        for item in queryset:
            if item.app_name in os.listdir():
                shutil.rmtree(item.app_name)
            item.delete()


admin.site.register(Projet, ProjetAdmin)
admin.site.register(Membre)
