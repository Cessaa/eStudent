from django.contrib import admin
from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('create/', views.CreateStudent.as_view(), name='create'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='delete'),
]
