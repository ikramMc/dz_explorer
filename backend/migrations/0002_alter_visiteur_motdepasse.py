# Generated by Django 4.1.4 on 2023-05-24 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visiteur',
            name='motDePasse',
            field=models.CharField(max_length=500),
        ),
    ]
