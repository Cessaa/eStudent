
from django.contrib import admin
from django.urls import path, include

from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexStudent.as_view(), name="student/list"),
    path('student/', include("student.urls")),
]
