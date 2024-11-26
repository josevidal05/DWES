from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Tlibros, Tcomentarios

# Create your views here.
def pagina_de_prueba(request):
    return HttpResponse("<h1>Hola caracola</h1>"); 

def devolver_libros(request):
    lista = Tlibros.objects.all()
    respuesta_final = []
    for fila_sql in lista:
        diccionario = {}
        diccionario['id'] = fila_sql.id
        diccionario['nombre'] = fila_sql.nombre
        diccionario['autor'] = fila_sql.autor
        diccionario['año_publicacion'] = fila_sql.año_publicacion
        respuesta_final.append(diccionario)
    return JsonResponse(respuesta_final, safe=False)

def devolver_libro_por_id(request, id_solicitado):
    libro = Tlibros.objects.get(id=id_solicitado)
    comentarios = libro.tcomentarios_set.all()
    lista_comentarios= []
    for fila_comentario_sql in comentarios:
        diccionario = {}
        diccionario['id'] = fila_comentario_sql.id
        diccionario['comentario'] = fila_comentario_sql.comentario
        diccionario['libro']=fila_comentario_sql.libro.nombre
        lista_comentarios.append(diccionario)
    resultado= {
        'id':libro.id,
        'nombre':libro.nombre,
        'autor':libro.autor,
        'año_publicacion':libro.año_publicacion,
        'comentarios':lista_comentarios
    }
    return JsonResponse(resultado, json_dumps_params={'ensure_ascii':False})

@csrf_exempt
def guardar_comentario(request, libro_id):
    if request.method != 'POST':
        return None
    
    json_peticion = json.loads(request.body)
    comentario = Tcomentarios()
    comentario.comentario = json_peticion['nuevo_comentario']
    comentario.libro = Tlibros.objects.get(id=libro_id)
    comentario.save()
    return JsonResponse({"status":"ok"})