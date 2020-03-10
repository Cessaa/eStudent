from django.shortcuts import render, get_object_or_404
from .forms import StudentForm
from django.http import HttpResponseRedirect, HttpResponse
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
            messages.add_message(request, messages.SUCCESS, "Kayit Basarili.")
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(status=302)
    else:
        form = StudentForm()
    return render(request, 'create.html', {'form': form})


def edit(request,id):
    student = get_object_or_404(Student,student_id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        student = form.save(commit=False)
        student.save()
        messages.add_message(request, messages.INFO, 'Güncelleme başarılı.')
        return HttpResponseRedirect('/')

    return render(request, "edit.html", {"form": form})


def delete(request, id):
    student = get_object_or_404(Student, student_id=id)
    student.delete()
    messages.add_message(request, messages.WARNING, 'Silme işlemi başarılı.')
    return HttpResponseRedirect('/')
