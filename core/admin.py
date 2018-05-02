from django.contrib import admin

from core.models import Projet, Membre


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'etat')
    list_filter = ('etat', 'phare')
    search_fields = ('nom',)
    ordering = ('nom',)
    prepopulated_fields = {'slug': ('nom',), }
    fieldsets = (
        ('Informations Générales', {
            # définis les champs qui y sont représenter
            'fields': ('nom', 'slug', 'description', 'header')
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
            'fields': ('etat', 'phare',)
        }),

    )


admin.site.register(Projet, ProjetAdmin)
admin.site.register(Membre)
