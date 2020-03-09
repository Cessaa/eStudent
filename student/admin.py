from django.contrib import admin
from .models import Student

# Register your models here.

def associate(obj):
    return "{} {}".format(obj.firstName, obj.lastName)


class StudentAdmin(admin.ModelAdmin):

    list_display = (associate, "student_id")
    search_fields = ["firstName", "lastName", "student_id"]


admin.site.register(Student, StudentAdmin)
