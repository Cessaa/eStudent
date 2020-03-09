
from django.contrib import admin
from django.urls import path, include

from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list, name="student/list"),
    path('student/', include("student.urls")),
]
