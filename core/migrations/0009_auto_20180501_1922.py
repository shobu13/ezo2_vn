# Generated by Django 2.0.3 on 2018-05-01 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180501_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='etat',
            field=models.BooleanField(default=False, verbose_name='Terminé ?'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='chef',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chef', to='core.Membre', verbose_name='chef de projet'),
        ),
    ]