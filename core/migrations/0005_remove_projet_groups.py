# Generated by Django 2.0.3 on 2018-05-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_projet_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='groups',
        ),
    ]
