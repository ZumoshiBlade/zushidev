from django.shortcuts import render
from core.models import *

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def proyectos(request):
    context = {"lista_proyectos" : Proyecto.objects.all()}
    return render(request, "core/proyectos.html", context)