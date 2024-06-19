from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apartment/<int:id>/', views.apartment_detail, name='apartment_detail'),
    path('apartment/add/', views.apartment_create, name='apartment_create'),
    path('apartment/edit/<int:id>/', views.apartment_edit, name='apartment_edit'),
    path('register/', views.register, name='register'),
]
