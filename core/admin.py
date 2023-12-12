from django.contrib import admin

# Register your models here.
from .models import Tecnologia, Proyecto, Tecnologia_Proyecto
    
# Registra tus modelos aquí
admin.site.register(Tecnologia)
admin.site.register(Proyecto)
admin.site.register(Tecnologia_Proyecto)