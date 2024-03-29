from django.contrib import admin
from django.urls import path
from . import views
from .routes import viewsAdmin

urlpatterns = [
    path('', views.home, name='home'),
    # path('administrador/contacto', viewsAdmin.index, name='contacto'),
    path('administrador/paginas', viewsAdmin.cargar_paginas, name='paginas'),


    ]