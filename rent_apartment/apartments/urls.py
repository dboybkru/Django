from django.urls import path
from . import views

urlpatterns = [
    path('', views.apartment_list, name='apartment_list'),
    path('new/', views.apartment_create, name='apartment_create'),
]
