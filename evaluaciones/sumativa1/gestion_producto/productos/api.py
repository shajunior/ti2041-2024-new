from ninja import NinjaAPI
from .models import Producto, Categoria, Marca
from typing import List
from pydantic import BaseModel  # Usamos Pydantic para validación

api = NinjaAPI()

# Definir el modelo Pydantic para la actualización de productos
class ProductoIn(BaseModel):
    codigo: str
    nombre: str
    precio: float
    categoria_id: int
    marca_id: int

# Servicio 1: Obtener todos los productos
@api.get("/productos", response=List[str])
def listar_productos(request):
    return [producto.nombre for producto in Producto.objects.all()]

# Servicio 2: Obtener detalles de un producto por ID
@api.get("/productos/{producto_id}")
def detalle_producto(request, producto_id: int):
    producto = Producto.objects.get(id=producto_id)
    return {
        "codigo": producto.codigo,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "categoria": producto.categoria.nombre,
        "marca": producto.marca.nombre,
    }

# Servicio 3: Actualizar un producto existente
@api.put("/productos/{producto_id}")
def actualizar_producto(request, producto_id: int, producto: ProductoIn):
    # Obtener el producto a actualizar
    try:
        producto_existente = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        return {"success": False, "message": "Producto no encontrado"}

    # Actualizar los campos del producto
    categoria = Categoria.objects.get(id=producto.categoria_id)
    marca = Marca.objects.get(id=producto.marca_id)

    producto_existente.codigo = producto.codigo
    producto_existente.nombre = producto.nombre
    producto_existente.precio = producto.precio
    producto_existente.categoria = categoria
    producto_existente.marca = marca

    # Guardar los cambios
    producto_existente.save()

    return {"success": True, "producto_id": producto_existente.id}

