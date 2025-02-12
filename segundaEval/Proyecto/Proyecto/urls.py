"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.authtoken.views import ObtainAuthToken
from django.urls import path
from Aplicacion.views import listar_eventos, crear_evento, actualizar_evento, eliminar_evento, listar_reservas, \
    crear_reservas, actualizar_estadoReservas, eliminar_reservas, listar_comentarios, crear_comentario, \
    registrar_usuario, login_usuario
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentación",
        default_version="v1",
        description="Documentación de la API",
    ),
    public=True,
    permission_classes=[AllowAny],
)


urlpatterns = [
path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('usuarios/login/', ObtainAuthToken.as_view(), name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('eventos/', listar_eventos.as_view(), name='listar_eventos'),
    path('eventos/crear/', crear_evento.as_view(), name='crear_evento'),
    path('eventos/actualizar/<str:titulo>/', actualizar_evento.as_view(), name='actualizar_evento'),
    path('eventos/eliminar/<str:id>/', eliminar_evento.as_view(), name='eliminar_evento'),
    path('reservas/<int:id>/', listar_reservas.as_view(), name='listar_reservas'),
    path('reservas/crear/', crear_reservas.as_view(), name='crear_reservas'),
    path('reservas/actualizar/<int:id>/', actualizar_estadoReservas.as_view(), name='actualizar_estadoReservas'),
    path('reservas/eliminar/<int:id>/', eliminar_reservas.as_view(), name='eliminar_reservas'),
    path('comentarios/<int:id>/', listar_comentarios.as_view(), name='listar_comentarios'),
    path('comentarios/crear/', crear_comentario.as_view(), name='crear_comentario'),
    path('usuarios/registrar/', registrar_usuario.as_view(), name='registrar_usuario'),
    path('login/', login_usuario.as_view(), name='login_usuario')
]
