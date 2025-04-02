from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from tienda.models import Frutas

# Create your views here.

def index(request):
    return HttpResponse("Hola mundo, esta es la pagina principal")

def frutas(request):
    if request.method == 'GET':
        frutas_disponibles = ["Manzana", "Banana", "Naranja", "Fresa"]
        return render(request, 'frutas.html', {'frutas': frutas_disponibles})
    
#############################

def fruta_form(request: HttpRequest):
    return render(request, 'fruteria.html')

def fruta_view(request: HttpResponse):
    return render (request, 'lista.html')

def fruta(request: HttpRequest):
    if request.method == 'POST':
        nombre: str = request.POST['nombre']
        precio: float = float(request.POST['precio'])
        distribuidora: str = request.POST['distribuidora']
        
        fruta: Frutas = Frutas.objects.create(
            nombre=nombre,
            precio=precio,
            distribuidora=distribuidora
        )
        fruta.save()
    fruteria: dict[str, str] = Frutas.objects.all()
    return render(request, 'lista.html', {'frutas':fruteria})
    
def eliminar_fruta(request, fruta_id):
    try:
        fruta = Frutas.objects.get(id=fruta_id)
        fruta.delete()
        return redirect('fruta')  # Redirige a la lista después de eliminar
    except Frutas.DoesNotExist:
        return HttpResponse('Fruta no encontrada', status=404)

def modificar_fruta(request, fruta_id):
    try:
        fruta = Frutas.objects.get(id=fruta_id)
        if request.method == 'POST':
            fruta.nombre = request.POST['nombre']
            fruta.precio = float(request.POST['precio'])
            fruta.distribuidora = request.POST['distribuidora']
            fruta.save()
            return redirect('fruta')
        return render(request, 'editar.html', {'fruta': fruta})
    except Frutas.DoesNotExist:
        return HttpResponse('Fruta no encontrada', status=404)
