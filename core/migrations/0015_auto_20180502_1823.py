# Generated by Django 2.0.3 on 2018-05-02 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180502_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Membre'),
        ),
    ]
