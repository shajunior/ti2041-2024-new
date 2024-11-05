from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Configurar el login como la página raíz
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Las demás rutas que ya tienes
    path('register/', views.register, name='register'),
    path('result/<int:producto_id>/', views.result, name='result'),
    path('product/<int:producto_id>/', views.product_detail, name='product_detail'),
    path('product/edit/<int:producto_id>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:producto_id>/', views.product_delete, name='product_delete'),
]
