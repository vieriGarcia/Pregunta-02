from django.shortcuts import render
from datetime import datetime, timedelta
from servicios.models import Servicio
from Ruteo.settings import MEDIA_ROOT
import re
# Vistas de Ruteo

def inicio(request):
	fecha= datetime.now().strftime("%d-%m-%y %H:%M:%S")
	return render(request,"Content/inicio.html",{"fecha":fecha})

def nosotros(request):
	return render(request,"Content/nosotros.html")

def servicios(request):
	services= Servicio.getAll()
	#path_media=MEDIA_ROOT.replace('\\','/')+"/"
	return render(request,"Content/servicios.html",{"servicios":services})