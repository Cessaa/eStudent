from django.shortcuts import render,get_object_or_404
from .forms import StudentForm
from django.http import HttpResponseRedirect
from .models import Student
from django.contrib import messages


def list(request):
    students = Student.objects.all()
    data = {
        'object_list': students
    }
    return render(request, 'list.html', data)


def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return HttpResponseRedirect('/')
    else:
        form = StudentForm()
    return render(request, 'create.html', {'form': form})


def edit(request,id):
    student = get_object_or_404(Student,student_id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        student = form.save(commit=False)
        student.save()
        return HttpResponseRedirect('/')

    return render(request,"edit.html", {"form":form})


def delete(request,id):
    student = get_object_or_404(Student, student_id = id)
    student.delete()
    return HttpResponseRedirect('/')