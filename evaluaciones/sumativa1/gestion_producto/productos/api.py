from ninja import NinjaAPI
from ninja.security import HttpBearer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Producto, Categoria, Marca
from typing import List
from pydantic import BaseModel

# Configuración de seguridad con JWT
class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            RefreshToken(token)
            return token
        except Exception:
            return None

api = NinjaAPI(auth=JWTAuth())

# Modelo Pydantic para los servicios
class ProductoIn(BaseModel):
    codigo: str
    nombre: str
    precio: float
    categoria_id: int
    marca_id: int

class ProductoOut(BaseModel):
    id: int
    codigo: str
    nombre: str
    precio: float
    categoria: str
    marca: str

# Servicio 1: Generar un Token JWT
@api.post("/token")
def obtener_token(request, username: str, password: str):
    from django.contrib.auth.models import User
    from django.contrib.auth import authenticate

    user = authenticate(username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return {"access": str(refresh.access_token), "refresh": str(refresh)}
    return {"error": "Credenciales inválidas"}

# Servicio 2: Obtener todos los productos
@api.get("/productos", response=List[ProductoOut])
def listar_productos(request):
    return [
        ProductoOut(
            id=producto.id,
            codigo=producto.codigo,
            nombre=producto.nombre,
            precio=producto.precio,
            categoria=producto.categoria.nombre,
            marca=producto.marca.nombre,
        )
        for producto in Producto.objects.all()
    ]

# Servicio 3: Crear un producto
@api.post("/productos", response=ProductoOut)
def crear_producto(request, producto: ProductoIn):
    categoria = Categoria.objects.get(id=producto.categoria_id)
    marca = Marca.objects.get(id=producto.marca_id)
    nuevo_producto = Producto.objects.create(
        codigo=producto.codigo,
        nombre=producto.nombre,
        precio=producto.precio,
        categoria=categoria,
        marca=marca,
    )
    return ProductoOut(
        id=nuevo_producto.id,
        codigo=nuevo_producto.codigo,
        nombre=nuevo_producto.nombre,
        precio=nuevo_producto.precio,
        categoria=nuevo_producto.categoria.nombre,
        marca=nuevo_producto.marca.nombre,
    )

# Servicio 4: Actualizar un producto
@api.put("/productos/{producto_id}")
def actualizar_producto(request, producto_id: int, producto: ProductoIn):
    try:
        producto_existente = Producto.objects.get(id=producto_id)
    except Producto.DoesNotExist:
        return {"error": "Producto no encontrado"}

    producto_existente.codigo = producto.codigo
    producto_existente.nombre = producto.nombre
    producto_existente.precio = producto.precio
    producto_existente.categoria = Categoria.objects.get(id=producto.categoria_id)
    producto_existente.marca = Marca.objects.get(id=producto.marca_id)
    producto_existente.save()

    return {"success": True, "producto_id": producto_existente.id}

# Servicio 5: Eliminar un producto
@api.delete("/productos/{producto_id}")
def eliminar_producto(request, producto_id: int):
    try:
        producto = Producto.objects.get(id=producto_id)
        producto.delete()
        return {"success": True}
    except Producto.DoesNotExist:
        return {"error": "Producto no encontrado"}

