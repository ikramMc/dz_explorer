# Generated by Django 4.1.4 on 2023-05-24 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_pointinteret_heureouverture'),
    ]

    operations = [
        migrations.AddField(
            model_name='moyentransport',
            name='PiId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.pointinteret'),
        ),
    ]
