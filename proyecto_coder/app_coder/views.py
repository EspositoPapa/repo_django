from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso
from django.template import Template
# Create your views here.

def curso(request):
    cursos= Curso.objects.all()#toda la data de mi BD#
    datos={"cursos":cursos}
    plantilla=loaer.get_template("plantilla.html")
    documento=plantilla.render(datos)

    return HttpResponse(cursos)

def alta_curso(request,nombre):
    curso=Curso(nombre="JS",camada=287318)
    curso.save()
    texto= f"Se guardo en la BD el curso:{curso.nombre} Camada:{curso.camada}"
    return HttpResponse(texto)
