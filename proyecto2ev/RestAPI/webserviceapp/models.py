from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    es_organizador = models.BooleanField(default=False)
    es_participante = models.BooleanField(default=True)

class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos')

class Reserva(models.Model):
    PENDIENTE = 'pendiente'
    CONFIRMADA = 'confirmada'
    CANCELADA = 'cancelada'

    ESTADOS = [
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADA, 'Confirmada'),
        (CANCELADA, 'Cancelada'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    entradas_reservadas = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default=PENDIENTE)

class Comentario(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
