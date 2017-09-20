# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoclase', '0003_auto_20170906_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='CursoFprop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('inicio_curso', models.DateTimeField()),
                ('termino_curso', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoClaseFprop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_id', models.CharField(max_length=42)),
                ('pub_data', models.DateTimeField(verbose_name='date published')),
                ('tipo_de_archivo', models.CharField(max_length=10)),
                ('descarga', models.URLField(verbose_name='Archivo de adescarga')),
                ('curso_fptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoclase.CursoFprop')),
            ],
        ),
        migrations.DeleteModel(
            name='VideoClase',
        ),
    ]
