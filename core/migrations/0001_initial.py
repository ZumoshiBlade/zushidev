# Generated by Django 5.0 on 2023-12-14 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_prod', models.DateField()),
                ('sitio_web', models.CharField(null=True)),
                ('imagen', models.ImageField(null=True, upload_to='proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia_Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proyecto')),
                ('tecnologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tecnologia')),
            ],
        ),
    ]
