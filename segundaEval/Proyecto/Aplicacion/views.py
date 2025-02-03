from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from models import User, Event, Reserva, Comentario


def listar_eventos(request):
    evento = Reserva.objects.all()
    data = [{"titulo": e.titulo, "descripcion": e.descripcion, "fecha": e.fecha_hora, } for e in evento]
    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_evento(request):



    if request.method == "POST":
            data = json.loads(request.body)
            if data["rol"] == "Organizador":
                # Comporbar si el evento existe

                evento = Event.objects.create(
                    titulo=data["titulo"],
                    descripcion=data["descripcion"],
                    fecha_hora=data["fecha_hora"],
                    capacidad_maxima=data["capacidad_maxima"],
                    imagen_url=data["imagen_url"],
                    organizador=data["organizador"],
                )
                return JsonResponse({"titulo": evento.titulo, "mensaje":
                    "Producto creado exitosamente"})
            return JsonResponse ({"error": "El evento ya existe" })


@csrf_exempt
def actualizar_evento(request, titulo):
    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)
        evento = Event.objects.get(titulo=titulo)
        evento.descripcion = data.get("descripcion", evento.descripcion)
        evento.fecha_hora = data.get("fecha_hora", evento.fecha_hora)
        evento.capacidad_maxima = data.get("capacidad_maxima", evento.capacidad_maxima)
        evento.imagen_url = data.get("imagen_url", evento.imagen_url)
        evento.organizador = data.get("organizador", evento.organizador)
        evento.created_at = data.get("created_at", evento.created_at)
        evento.save()
        return JsonResponse({"mensaje": "Producto actualizado"})


@csrf_exempt
def eliminar_evento(request, titulo):
    if request.method == "DELETE":
        evento = Event.objects.get(titulo=titulo)
        evento.delete()
        return JsonResponse({"mensaje": "Producto eliminado"})


# /**** RESERVAS ******/

def listar_reservas(request):
    usuario = User.objects.get(id=id)
    reservas = Reserva.objects.select_related('evento').filter(usuario=usuario)

    data = [{
            "id": r.id,
            "usuario": r.usuario.username,
            "evento": r.evento.titulo,
            "entradas": r.cantidad_entradas,
            "estado": r.estado
    } for r in reservas]
    return JsonResponse(data, safe=False)

@csrf_exempt
def crear_reservas(request):

    if request.method == "POST":
        data = json.loads(request.body)

        # Comprobar que los datos necesarios están presentes
        campos_requeridos = ["usuario_id", "evento_id", "cantidad_entradas",
                             "evento"]
        for campo in campos_requeridos:
            if campo not in data or not data[campo]:
                return JsonResponse({"error": f"Falta el campo requerido: {campo}"})

        # Comprobar que el usuario_id es un entero
        try:
            usuario_id = int(data.get("usuario_id"))
        except (ValueError, TypeError):
            return JsonResponse({"error": "El usuario_id debe ser un número entero"})

        # Comprobar que el usuario existe
        if not User.objects.filter(id=usuario_id).exists():
            return JsonResponse({"error": "El usuario no existe"})

        # Comprobar que el evento existe
        if not Reserva.objects.filter(id=data.get("evento_id")).exists():
            return JsonResponse({"error": "El evento no existe"})

        reserva = Reserva.objects.create(
            usuario=User.data.get(id=data["usuario"]),
            evento=Event.data.get(id=data["evento"]),
            cantidad_entradas=data["cantidad_entradas"],
            estado=data["estado"],
        )
        return JsonResponse({"titulo": reserva.titulo, "mensaje": "Producto creado exitosamente"})


@csrf_exempt
def actualizar_estadoReservas(request, id):
    if request.method in ["PUT", "PATCH"]:
        data = json.loads(request.body)

        reserva = Reserva.objects.get(id=id)
        reserva.estado = data.get("estado", reserva.estado)
        reserva.save()
        return JsonResponse({"mensaje": "Estado actualizado"})


@csrf_exempt
def eliminar_reservas(request, id):
    if request.method == "DELETE":
        reserva = Reserva.objects.get(id=id)
        reserva.delete()
        return JsonResponse({"mensaje": "Reserva eliminada"})
