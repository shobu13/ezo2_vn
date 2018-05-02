# Generated by Django 2.0.3 on 2018-05-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_projet_scenariste'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='couleur_tab_active_background',
            field=models.CharField(blank=True, default='#f3e5f5', max_length=7),
        ),
        migrations.AddField(
            model_name='projet',
            name='couleur_tab_soulignement',
            field=models.CharField(blank=True, default='#4a148c', max_length=7),
        ),
        migrations.AddField(
            model_name='projet',
            name='couleur_tab_texte',
            field=models.CharField(blank=True, default='#d500f9', max_length=7),
        ),
    ]