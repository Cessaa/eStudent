from django.contrib import admin
from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('create/', views.CreateStudent.as_view(), name='create'),
    path('edit/<int:id>', views.UpdateStudent.as_view(), name='edit'),
    path('delete/<int:id>', views.DeleteStudent.as_view(), name='delete'),
]
