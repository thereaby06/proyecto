from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import RegisterForm
from .models import Producto
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def incrementar_cantidad(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.cantidad += 1
    producto.save()
    return redirect('productos')

@login_required
def decrementar_cantidad(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if producto.cantidad > 0:
        producto.cantidad -= 1
        producto.save()
    return redirect('productos')


@login_required
def productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(codigo__icontains=query) |
            Q(producto__icontains=query) |
            Q(descripcion__icontains=query)
        )
    else:
        productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'query': query})

@login_required
def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'ingresar_producto.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def servicios(request):
    return render(request, 'servicios.html')

@login_required
def contactos(request):
    return render(request, 'contactos.html')

# Nueva vista para "Mi Perfil"
@login_required
def perfil(request):
    return render(request, 'perfil.html')

# Vista para logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
