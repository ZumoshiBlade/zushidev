# Generated by Django 5.0 on 2023-12-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_tecnologia_proyecto_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='proyectos'),
        ),
    ]
