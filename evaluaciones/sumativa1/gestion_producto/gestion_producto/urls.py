
from django.contrib import admin
from django.urls import path, include  # Importa include
from productos import views as productos_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', productos_views.user_login, name='login'),  # Página de login
    path('productos/', include('productos.urls')),  # Incluye las rutas de productos
    path('logout/', productos_views.user_logout, name='logout'),  # Ruta para cerrar sesión
    path('register/', productos_views.register, name='register'),  # Ruta para registrar productos
]



