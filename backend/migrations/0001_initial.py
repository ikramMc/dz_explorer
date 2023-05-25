# Generated by Django 4.1.4 on 2023-05-19 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoyenTransport',
            fields=[
                ('idMoyenTrasport', models.AutoField(primary_key=True, serialize=False)),
                ('categorie', models.CharField(max_length=50)),
                ('NombrePassagers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Visiteur',
            fields=[
                ('idVisiteur', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=60)),
                ('Prenom', models.CharField(max_length=60)),
                ('Pays', models.CharField(max_length=45)),
                ('NumTel', models.CharField(default='Null', max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('motDePasse', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='PointInteret',
            fields=[
                ('idPoint', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=60)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('heureOuverture', models.CharField(blank=True, max_length=10, null=True)),
                ('heureFermeture', models.TimeField()),
                ('rate', models.IntegerField()),
                ('categorie', models.CharField(max_length=25)),
                ('theme', models.CharField(max_length=45)),
                ('regionId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.region')),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('idEvenement', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=80)),
                ('Description', models.CharField(max_length=400)),
                ('DateDebut', models.DateField()),
                ('DateFin', models.DateField()),
                ('DatePublication', models.DateField(default='2022-05-02')),
                ('PiId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.pointinteret')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('idCommentaire', models.AutoField(primary_key=True, serialize=False)),
                ('Contenu', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('PiId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.pointinteret')),
                ('visiteurId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.visiteur')),
            ],
        ),
    ]