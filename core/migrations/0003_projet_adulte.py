# Generated by Django 2.0.3 on 2018-05-18 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_projet_app_is_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='adulte',
            field=models.BooleanField(default=False, verbose_name='Adulte ?'),
        ),
    ]