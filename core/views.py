from django.shortcuts import render
from core.models import *

# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    context = {"lista_proyectos": proyectos}
    return render(request, "core/home.html", context)

