from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Usuario, Evento, Reserva, Comentario

admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(Reserva)
admin.site.register(Comentario)
