#NO ESTA EN USO PORQUE SE CREÓ UNA APP PARA INICIO

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'inicio.html')
