from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def electronica(request):
    data = {
        'titulo': 'Electrónica',
        'producto1': 'Televisor',
        'producto2': 'Radio',
        'producto3': 'Computadora',
    }
    return render(request, 'productos.html', data)

def juguetes(request):
    data = {
        'titulo': 'Juguetes',
        'producto1': 'Auto',
        'producto2': 'Pelota de Futbol',
        'producto3': 'Figura de acción',
    }
    return render(request, 'productos.html', data)

def ropa(request):
    data = {
        'titulo': 'Ropa',
        'producto1': 'Pantalones',
        'producto2': 'Chaqueta',
        'producto3': 'Camisa',
    }
    return render(request, 'productos.html', data)

