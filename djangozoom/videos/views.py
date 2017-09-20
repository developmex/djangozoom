# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
import os, sys
lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)
from django.views.generic import TemplateView



class VideoClaseTempateView(TemplateView):
    template = "index.html"

    def get_context_data(self, *args,**kwargs):
        context = super(VideoClassTempateView, self).get_context_data(*args, **kwargs)
        context["titulo"] = "Titulo de Contexto Video Clase"
        return context




def index(request):


    with open('static/datos.json') as json_data:
        data = json.load(json_data)

    template =  'index.html'

    a = "Saludos esta es una cadena !"
    meetings = data['meetings']
    recording = data['meetings']

    # Create a list to place the dictionary keys in


    # For each key in the dictionary's keys,


    context = {
        'cadena': a,
        'datos': data['meetings'],
        'meetings': meetings,
        'recording': recording[0]
    }

    return render(request, template, context)


def contenido(request):
    pass
    template = "contenido.html"



    with open('static/datos.json') as json_data:
        data = json.load(json_data)


        sub = data['meetings']



    context = {
        "tabla": data['meetingst'],
        "tabla2": sub[0]
    }
    return render(request, template, context)

