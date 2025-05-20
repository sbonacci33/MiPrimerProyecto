from django.shortcuts import render

def inicio_view(request):
    return render(request, 'inicio.html')

def saludo_view(request):
    return render(request, 'poema.html')

