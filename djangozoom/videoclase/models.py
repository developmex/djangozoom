# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json
# Create your models here.

from zoomus import ZoomClient
class CursoFprop(models.Model):
    nombre = models.CharField(max_length=20, blank=False)
    inicio_curso = models.DateTimeField()
    termino_curso = models.DateTimeField()


    def __str__(self):

        return self.nombre


class Meeting(models.Model):

    pass
    client = ZoomClient('g7MZBr7GT3CdFn07F1F2Bw', 'jEJouAV2JgKAEHLHe0eQogUL7yvKHHaDXY3y')
    host_id = "7pCPQl2tSC-S9QoSbZ3RHA"

    lista = client.meeting.list

    numero_de_meeting = models.CharField(max_length=30)
    with open('static/datos.json') as f:
        data =json.load(f)
    meeting_lista = data


    slug = models.SlugField(max_length=100,default=numero_de_meeting)



    def __str__(self):

        return self.numero_de_meeting


class VideoClaseFprop(models.Model):
    meeting_numero = models.ForeignKey(Meeting, on_delete=models.CASCADE),
    curso_fptop = models.ForeignKey(CursoFprop, on_delete=models.CASCADE)
    meeting_id = models.CharField(max_length=42)
    pub_data = models.DateTimeField('date published')
    tipo_de_archivo = models.CharField(max_length=10)
    descarga = models.URLField(verbose_name="Archivo de Descarga")

    def __str__(self):

        return self.curso_fptop

