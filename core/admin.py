from django.contrib import admin


from core.models import Projet, Membre


class ProjetAdmin(admin.ModelAdmin):

    list_display = ('nom', 'chef', 'etat')
    list_filter = ('chef', 'etat')
    search_fields = ('nom', )
    ordering = ('nom', )
    prepopulated_fields = {'slug': ('nom',), }


admin.site.register(Projet, ProjetAdmin)
admin.site.register(Membre)
