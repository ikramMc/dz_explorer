# Generated by Django 4.1.4 on 2023-05-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_visiteur_prenom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visiteur',
            name='NumTel',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='visiteur',
            name='Prenom',
            field=models.CharField(max_length=60, null=True),
        ),
    ]