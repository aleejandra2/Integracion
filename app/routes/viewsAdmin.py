from django.shortcuts import render

def cargar_paginas(request):
  return render(request, 'administrador/paginas/index.html')