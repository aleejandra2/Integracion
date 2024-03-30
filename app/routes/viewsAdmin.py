from django.shortcuts import render

def cargar_paginas(request):
  return render(request, 'administrador/paginas/index.html')

def cargar_contacto(request):
  return render(request, 'administrador/contacto/index.html')
  
def cargar_nosotros(request):
  return render(request, 'administrador/nosotros/index.html')  