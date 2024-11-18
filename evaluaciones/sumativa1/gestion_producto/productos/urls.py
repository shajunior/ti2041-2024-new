from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='productos'),
    path('register/', views.register, name='register'),  # Asegúrate de que esta ruta existe y tiene el nombre 'register'
    path('result/<int:producto_id>/', views.result, name='result'),
    path('product/<int:producto_id>/', views.product_detail, name='product_detail'),
    path('product/edit/<int:producto_id>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:producto_id>/', views.product_delete, name='product_delete'),
]
