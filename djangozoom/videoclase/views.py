# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView
import json
from .models import CursoFprop
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Meeting
from zoomus import ZoomClient
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.




def index(request):
    with open('static/datos.json') as json_data:
        data = json.load(json_data)

    template = 'index.html'

    a = "Saludos esta es una cadena !"
    meetings = data['meetings']
    recording = data['meetings']
    videosguardados = CursoFprop
    # Create a list to place the dictionary keys in


    # For each key in the dictionary's keys,


    context = {

        'datos': data['meetings'],
        'meetings': meetings,
        'recording': recording[0],
        'meeting_id': videosguardados
    }

    return render(request, template, context)



class MeetingListView(ListView):
    model = Meeting
    meetin_number = Meeting.numero_de_meeting
    context_object_name = 'my_book_list'  # your own name for the list as a template variable
    queryset = Meeting.data['meetings'] # Get 5 books containing the title war
    template_name = 'videoclase/meeting_list.html'  # Specify your own template name/location
    rx = Meeting.data


    def get_context_data(self, **kwargs):

        context = super(MeetingListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class MeetingDetailView(DetailView):
    model = Meeting
    nombre = Meeting.numero_de_meeting
    host_id = "7pCPQl2tSC-S9QoSbZ3RHA"
    client = ZoomClient('g7MZBr7GT3CdFn07F1F2Bw', 'jEJouAV2JgKAEHLHe0eQogUL7yvKHHaDXY3y', host_id)

    lista = client.meeting
    meeting = lista.get(id='268601917',host_id='7pCPQl2tSC-S9QoSbZ3RHA')
    print(meeting)
    context_object_name = 'meetings'  # your own name for the list as a template variable
    # Get 5 books containing the title war
    template_name = 'videoclase/meeting_detail.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        context = super(MeetingDetailView, self).get_context_data(**kwargs)
        context['meeting'] = self.meeting
        context['lista'] = self.lista

        return context


class Meeting2DetailView(DetailView):
    model = Meeting
    nombre = Meeting.numero_de_meeting

    context_object_name = 'meetings'  # your own name for the list as a template variable
    # Get 5 books containing the title war
    template_name = 'videoclase/cliente_detail.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        host_id = "7pCPQl2tSC-S9QoSbZ3RHA"
        context = super(Meeting2DetailView, self).get_context_data(**kwargs)
        context['nombre'] = Meeting.numero_de_meeting
        context['datos'] = Meeting.data
        context['lista'] = Meeting.lista(host_id="7pCPQl2tSC-S9QoSbZ3RHA")
        context['slug'] = Meeting.slug
        return context


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'index.html')

    else:
        return render(request, 'index_404.html')

@login_required
def woerdpress(request):
    with open('static/datos.json') as json_data:
        data = json.load(json_data)

    template = 'temario_w.html'


    # Create a list to place the dictionary keys in


    # For each key in the dictionary's keys,


    context = {


    }

    return render(request, template, context)



def inicio(request):
    template = 'inicio.html'
    saludos = "Buenos dias"
    context = {
        'saluds':saludos

    }

    return render(request, template, context)