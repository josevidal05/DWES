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
from django.urls import path
from Aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/actualizar/<str:titulo>/', views.actualizar_evento, name='actualizar_evento'),
    path('eventos/eliminar/<str:titulo>/', views.eliminar_evento, name='eliminar_evento'),
    path('reservas/<int:id>/', views.listar_reservas, name='listar_reservas'),
    path('reservas/crear/', views.crear_reservas, name='crear_reservas'),
    path('reservas/actualizar/<int:id>/', views.actualizar_estadoReservas, name='actualizar_estadoReservas'),
    path('reservas/eliminar/<int:id>/', views.eliminar_reservas, name='eliminar_reservas'),
    path('comentarios/<int:id>/', views.listar_comentarios, name='listar_comentarios'),
    path('comentarios/crear/<int:id>/', views.crear_comentario, name='crear_comentario'),
    path('usuarios/registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('usuarios/login/', views.login_usuario, name='login_usuario')
]
