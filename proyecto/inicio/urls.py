from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_view, name='inicio'),        # muestra inicio.html
    path('saludo/', views.saludo_view, name='saludo'),  # muestra poema.html
]
