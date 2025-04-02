"""
URL configuration for pagina project.

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
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frutas/', views.frutas, name='frutas'),
    path('', views.fruta_form),
    path('fruteria', views.fruta, name='fruta'),
    path('fruteria/eliminar/<int:fruta_id>/', views.eliminar_fruta, name='eliminar_fruta'),
    path('fruteria/modificar/<int:fruta_id>/', views.modificar_fruta, name='modificar_fruta'),
]
