from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
from .models import *
import hashlib

from rest_framework.permissions import BasePermission

#**************************************************************************

# ROLES

class EsOrganizador(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.rol=="organizador"

class EsParticipante(BasePermission):
        def has_permission(self, request, view):
            return request.user and request.user.rol == "participante"

#****************************************************************************

class listar_eventos(APIView):
    permission_classes = [EsParticipante]

    @swagger_auto_schema(
        operation_description="Lista eventos filtrados por título o fecha.",
        manual_parameters=[
            openapi.Parameter('titulo', openapi.IN_QUERY, description="Filtrar por título", type=openapi.TYPE_STRING),
            openapi.Parameter('fecha', openapi.IN_QUERY, description="Filtrar por fecha (YYYY-MM-DD)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('pagina', openapi.IN_QUERY, description="Número de página", type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response(description="Lista de eventos")}
    )

    def get(self, request):
        titulo = request.GET.get("titulo", "")  # Filtrar por nombre
        orden = request.GET.get("orden", "titulo")  # Ordenar por el campo especificado
        limite = int(request.GET.get("limite", 10))  # Resultados por página
        pagina = int(request.GET.get("pagina", 1))  # Página actual

        # Filtrar y ordenar productos
        evento = Event.objects.filter(titulo__icontains=titulo).order_by(orden)
        # Paginación
        paginator = Paginator(evento, limite)  # Dividir productos en páginas de tamaño `limite`

        try:
            productos_pagina = paginator.page(pagina)  # Obtener los productos de la página actual
        except Exception as e:
            return Response({"error": str(e)}, status=400)  # Manejar errores de paginación

        # Crear respuesta con datos paginados
        data = {
            "count": paginator.count,  # Número total de productos
            "total_pages": paginator.num_pages,  # Número total de páginas
            "current_page": pagina,  # Página actual
            "next": pagina + 1 if productos_pagina.has_next() else None,  # Página siguiente
            "previous": pagina - 1 if productos_pagina.has_previous() else None,  # Página anterior
            "results": [
                {
                    "id": p.id,
                    "titulo": p.titulo,
                    "descripción": p.descripcion,
                    "fecha_hora":p.fecha_hora,
                    "capacidad_maxima": p.capacidad_maxima,

                } for p in productos_pagina
            ]  # Resultados actuales
        }

        return Response(data)


class crear_evento(APIView):
    permission_classes = [EsOrganizador]

    @swagger_auto_schema(
        operation_description="Crea un nuevo evento.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(type=openapi.TYPE_STRING, description='Título del evento'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripción del evento'),
                'fecha_hora': openapi.Schema(type=openapi.TYPE_STRING, format="date-time",
                                             description='Fecha y hora del evento'),
                'capacidad': openapi.Schema(type=openapi.TYPE_INTEGER, description='Capacidad máxima de asistentes'),
            },
            required=['titulo', 'descripcion', 'fecha_hora', 'capacidad']
        ),
        responses={201: openapi.Response(description="Evento creado"),
                   403: openapi.Response(description="No tienes permisos para crear eventos.")}
    )
    def post(self, request):

        data = request.data

        # Comprobar si el evento existe
        if Event.objects.filter(titulo=data["titulo"]).exists():
            return Response({"error": "El evento ya existe"})

        evento = Event.objects.create(
            titulo=data["titulo"],
            descripcion=data["descripcion"],
            fecha_hora=data["fecha_hora"],
            capacidad_maxima=data["capacidad_maxima"],
            imagen_url=data["imagen_url"],

            organizador=User.objects.get(username= data["organizador"]),
        )
        return Response({"titulo": evento.titulo, "mensaje":
            "Producto creado exitosamente"})

        return Response ({"error": "El evento ya existe" })


class actualizar_evento(APIView):
    permission_classes = [EsOrganizador]
    def put(self, request, titulo):
        data = request.data
        evento = Event.objects.select_related("organizador").get(titulo=titulo)

        evento.descripcion = data.get("descripcion", evento.descripcion)
        evento.fecha_hora = data.get("fecha_hora", evento.fecha_hora)
        evento.capacidad_maxima = data.get("capacidad_maxima", evento.capacidad_maxima)
        evento.imagen_url = data.get("imagen_url", evento.imagen_url)
        evento.organizador = User.objects.get(username=data["organizador"])
        evento.save()
        return Response({"mensaje": "Producto actualizado"})

    def patch(self, request, titulo):
        data = request.data
        evento = Event.objects.select_related("organizador").get(titulo=titulo)

        evento.descripcion = data.get("descripcion", evento.descripcion)
        evento.fecha_hora = data.get("fecha_hora", evento.fecha_hora)
        evento.capacidad_maxima = data.get("capacidad_maxima", evento.capacidad_maxima)
        evento.imagen_url = data.get("imagen_url", evento.imagen_url)
        evento.organizador = User.objects.get(username=data["organizador"])
        evento.save()
        return Response({"mensaje": "Producto actualizado"})



class eliminar_evento(APIView):
    permission_classes = [EsOrganizador]
    def delete(self, request, id):
        evento = Event.objects.get(id=id)
        evento.delete()
        return Response({"mensaje": "Producto eliminado"})


# /**** RESERVAS ******/

class listar_reservas(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        data = request.data
        usuario = User.objects.get(id=id)
        reservas = Reserva.objects.select_related('evento', 'usuario').filter(usuario=usuario)

        data = [{
                "id reserva": r.id,
                "usuario": r.usuario.username,
                "evento": r.evento.titulo,
                "entradas": r.cantidad_entradas,
                "estado": r.estado
        } for r in reservas]
        return Response(data)

class crear_reservas(APIView):
    permission_classes = [EsParticipante]

    @swagger_auto_schema(
        operation_description="Obtener lista de reservas",
        responses={200: openapi.Response("Lista de reservas")},
    )
    def post(self, request):
        data = request.data

        # Comprobar que los datos necesarios están presentes
        campos_requeridos = ["usuario", "evento", "cantidad_entradas",
                             "estado"]
        for campo in campos_requeridos:
            if campo not in data or not data[campo]:
                return Response({"error": f"Falta el campo requerido: {campo}"})

        # Comprobar que el usuario_id es un entero


        # Comprobar que el evento existe
        if not Event.objects.filter(id=data.get("evento")).exists():
            return Response({"error": "El evento no existe"})

        reserva = Reserva.objects.create(
            usuario=User.objects.get(id=data["usuario"]),
            evento=Event.objects.get(id=data["evento"]),
            cantidad_entradas=data["cantidad_entradas"],
            estado=data["estado"]
        )
        return Response({"id": reserva.id, "mensaje": "Reserva creado exitosamente"})


class actualizar_estadoReservas(APIView):
    permission_classes = [EsOrganizador]
    def put(self, request, id):
        data = request.data
        reserva = Reserva.objects.get(id=id)
        reserva.estado = data.get("estado", reserva.estado)
        reserva.save()
        return Response({"mensaje": "Estado actualizado"})

    def patch(self, request, id):
        data = request.data

        reserva = Reserva.objects.get(id=id)
        reserva.estado = data.get("estado", reserva.estado)
        reserva.save()
        return Response({"mensaje": "Estado actualizado"})



class eliminar_reservas(APIView):
    permission_classes = [EsParticipante]
    def delete(self, request, id):
        data = request.data
        reserva = Reserva.objects.get(id=id)
        reserva.delete()
        return Response({"mensaje": "Reserva eliminada"})


# /****** COMENTARIOS ******/

class listar_comentarios(APIView):
    def get(self, request, id):

    #ido = request.GET.get("ido")
    #print(ido)

    # Verificamos que el ID del usuario esté presente
        if not id:
            return Response({"error": "Se requiere el parámetro 'id' del usuario"})

        usuario = User.objects.get(id=id)
        comentario = Comentario.objects.select_related('evento').filter(usuario=usuario)

        data = [{
            "id": c.id,
            "usuario": c.usuario.username,
            "evento": c.evento.titulo,
            "texto": c.texto,
            "fecha_creacion": c.fecha_creacion
        } for c in comentario]
        return Response(data)


class crear_comentario(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        # Verificamos que los datos estén presentes en el cuerpo de la solicitud
        data = request.data
        if "texto" not in data or "fecha_creacion" not in data or "evento" not in data:
            return Response({"error": "Faltan datos requeridos (texto, fecha_creacion, evento)"})

        # Comprobamos que el usuario existe
        try:
            Usuario = User.objects.get(id=data["usuario"])
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"})

        # Comprobamos que el evento existe
        try:
            Evento = Event.objects.get(id=data["evento"])
        except Event.DoesNotExist:
            return Response({"error": "Evento no encontrado"})

        comentario = Comentario.objects.create(
            texto=data["texto"],
            fecha_creacion=data["fecha_creacion"],
            usuario=Usuario,
            evento=Evento,
        )

        return Response({
            "id": comentario.id,
            "mensaje": "Comentario creado exitosamente"
        })


#/****** USUARIOS **********/
def hash_contraseña(password):
    return make_password(password)

def check_contraseña(stored_hash, input_password):
    return stored_hash == make_password(input_password)


class registrar_usuario(APIView):
    def post(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"error": "Faltan datos requeridos (username, password)"}, status=400)

            # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return Response({"error": "El nombre de usuario ya está registrado"}, status=400)

        #hashear la contraseña
        hashed_password = hash_contraseña(password)

        User.objects.create(
            username=username,
            password = hashed_password

        )
        return Response({"mensaje": "Usuario registrado exitosamente"})


class login_usuario(APIView):
    def post(self, request):
        data = request.data
        username = data["username"]
        password = data["password"]

        usuario=User.objects.get(username=username)
        if not username or not password:
            return Response({"error": "Faltan datos requeridos (username, password)"}, status=400)

        try:
            #user = User.objects.get(username=username)
            if check_password(password, usuario.password):#encoded="pbkdf2_sha256"):
                return Response({"mensaje": "Login exitoso", "usuario": username})
            else:
                return Response({"error": "Contraseña incorrecta"})

        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado"})

