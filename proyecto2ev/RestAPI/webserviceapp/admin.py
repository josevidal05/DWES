from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User, Evento, Reserva, Comentario

@admin.register(User)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'tipo', 'biografia')
    list_filter = ('tipo',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'limiteMaximo', 'organizador')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('fecha', 'organizador')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'entradas')
    list_filter = ('estado',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'infoEvento', 'fecha')
    search_fields = ('texto',)
