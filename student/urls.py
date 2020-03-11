from django.contrib import admin
from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('create/', views.CreateView.as_view(), name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.DeleteView.as_view(), name='delete'),
]
