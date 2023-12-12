from django.db import models

# Create your models here.

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    fecha_prod = models.DateField()
    
    def __str__(self):
        return self.titulo
    
        
class Tecnologia_Proyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    tecnologia = models.OneToOneField(Tecnologia, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.proyecto.titulo} - {self.tecnologia.nombre}"
          
    
