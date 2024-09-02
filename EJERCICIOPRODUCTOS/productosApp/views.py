from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def calzado(request):
    data = {
        'titulo': 'Calzado',
        'producto1': 'Enzo Romeo',
        'producto2': 'Old West',
        'producto3': 'Worker Boots',
        'imagen1': 'images/enzoRomeo.png',
        'imagen2': 'images/oldWest.png',
        'imagen3': 'images/workerBoots.png',
    }
    return render(request, 'productos.html', data)

def armas(request):
    data = {
        'titulo': 'Armas',
        'producto1': 'Derringer',
        'producto2': 'Colt Navy 1851',
        'producto3': 'Remington 1858',
        'imagen1': 'images/derringer.png',
        'imagen2': 'images/coltNavy1851.png',
        'imagen3': 'images/remington1858.png',
    }
    return render(request, 'productos.html', data)

def ropa(request):
    data = {
        'titulo': 'Ropa',
        'producto1': 'Traje Azul',
        'producto2': 'Chaqueta de Duelo',
        'producto3': 'Gorro de vaquero',
        'imagen1': 'images/trajeazul.png',
        'imagen2': 'images/chaqueta.png',
        'imagen3': 'images/gorro.png',
    }
    return render(request, 'productos.html', data)

