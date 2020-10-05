from django.db import models

class Servicio(models.Model):
    id_servicio=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=25)
    descripcion=models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="images", blank=True, null=True)
    def getAll():
    	servicios=Servicio.objects.all().order_by('id_servicio')
    	return servicios
