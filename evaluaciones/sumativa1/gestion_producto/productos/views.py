from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm

# Gestión de productos

@login_required  # Vista para listar y filtrar productos, accesible solo para usuarios autenticados
def index(request):
    filter_value = request.GET.get('filter', '')
    productos = Producto.objects.filter(nombre__icontains=filter_value) if filter_value else Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

@login_required  # Vista para registrar un nuevo producto
def register(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('result', producto_id=producto.id)
    else:
        form = ProductoForm()
    return render(request, 'register.html', {'form': form})

@login_required  # Vista para mostrar resultados de registro
def result(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'result.html', {'producto': producto})

@login_required  # Vista para mostrar detalles de un producto
def product_detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'product_detail.html', {'producto': producto})

@login_required  # Vista para editar un producto
def product_edit(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('result', producto_id=producto.id)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'register.html', {'form': form})

@login_required  # Vista para eliminar un producto
def product_delete(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'product_delete.html', {'producto': producto})

# Autenticación de usuarios

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('productos')  # Redirige a la página de productos después de iniciar sesión
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirige a la página de login después de cerrar sesión
