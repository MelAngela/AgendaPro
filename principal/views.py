from django.shortcuts import render, redirect
from principal.forms import FormularioReservas
from principal.forms import FormularioProductos
from principal.models import Reserva, Estilista
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from functools import lru_cache

@lru_cache(maxsize=None)
def obtener_estilistas_disponibles():
    estilistas = Estilista.objects.filter(disponible=True)
    estilistas_disponibles = [estilista.nombre for estilista in estilistas]
    return estilistas_disponibles

def index(request):
    return render(request, 'index.html')

def servicios(request):
    return render(request, 'servicios.html')

def productos(request):
    return render(request, 'productos.html')

def listadoReservas(request):
    reservas = Reserva.objects.all()
    paginator = Paginator(reservas, 10)  # Mostrar 10 reservas por página
    page = request.GET.get('page')
    reservas = paginator.get_page(page)
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormularioReservas()
    if request.method == 'POST':
        form = FormularioReservas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reservas')
    data = {'form': form}
    return render(request, 'agregarReserva.html', data)

def agregarProducto(request):
    form = FormularioProductos()
    if request.method == 'POST':
        form = FormularioProductos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos')
   
    data = {'form': form}
    return render(request, 'agregarProducto.html', data)

def eliminarReserva(request, id):
    Reserva.objects.filter(id=id).delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    reserva = Reserva.objects.filter(id=id).first()
    form = FormularioReservas(instance=reserva)
    if request.method == 'POST':
        form = FormularioReservas(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('/reservas')
    data = {'form': form}
    return render(request, 'actualizarReserva.html', data)

def login(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/reservas')
        else:
            messages.error(request, 'Credenciales inválidas')
    
    return render(request, 'login.html')