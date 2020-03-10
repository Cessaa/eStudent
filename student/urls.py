from django.contrib import admin
from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('', views.list, name='list'),
    path('list', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]
