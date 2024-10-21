from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# 1. Vista para listar y filtrar productos
def index(request):
    filter_value = request.GET.get('filter', '')
    if filter_value:
        productos = Producto.objects.filter(nombre__icontains=filter_value)
    else:
        productos = Producto.objects.all()

    return render(request, 'index.html', {'productos': productos})

# 2. Vista para registrar un nuevo producto
def register(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('result', producto_id=producto.id)
    else:
        form = ProductoForm()

    return render(request, 'register.html', {'form': form})

# 3. Vista para mostrar resultados de registro
def result(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'result.html', {'producto': producto})

# 4. Vista para mostrar los detalles del producto
def product_detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'product_detail.html', {'producto': producto})

# 5. Vista para editar un producto
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

# 6. Vista para eliminar un producto
def product_delete(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')  # Redirige a la lista de productos

    return render(request, 'product_delete.html', {'producto': producto})