from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_register, name='list'),
    path('add/', views.add_register, name='add_register'),
    path('edit/<int:pk>/', views.edit_register, name='edit_register'),
    path('delete/<int:pk>/', views.delete_register, name='delete_register'),
]