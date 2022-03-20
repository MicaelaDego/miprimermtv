from django.http import HttpResponse
from django.template import Template, Context


def familia (request):
    return HttpResponse ('Esta es mi familia')

def pagina_inicio (request):
    archivo = open(r'C:\Users\micaela\Documents\python\DJANGO\MIPRIMERMVT\miprimermtv\miprimermtv\templates\page.html','r')
    nombre = 'Micaela'
    apellido = 'Dego'
    documento = 38004983 
    diccionario = {'nombre': nombre, 'apellido': apellido, 'documento': documento}

    plantilla = Template(archivo.read())
    archivo.close()
    context = Context(diccionario)
    documento = plantilla.render(context)
    return HttpResponse (documento)
