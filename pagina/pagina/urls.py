"""
URL configuration for pagina project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),
    path('logout/', views.user_logout, name='logout'),
    path('servicios/', views.servicios, name='servicios'),
    path('contactos/', views.contactos, name='contactos'),
    path('productos/', views.productos, name='productos'),
    path('ingresar_producto/', views.ingresar_producto, name='ingresar_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('incrementar_cantidad/<int:pk>/', views.incrementar_cantidad, name='incrementar_cantidad'),
    path('decrementar_cantidad/<int:pk>/', views.decrementar_cantidad, name='decrementar_cantidad'),
]


