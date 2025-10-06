from django.shortcuts import render
from .models import Contenido

def index(request):
    contenidos = Contenido.objects.all().order_by('contenido_id')
    return render(request, 'index.html', {'contenidos': contenidos})