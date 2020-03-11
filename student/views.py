from django.shortcuts import render, get_object_or_404
from .forms import StudentForm
from django.http import HttpResponseRedirect
from .models import Student
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin, InfoMessageMixin
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class IndexStudent(ListView):
    template_name = "list.html"
    model = Student
    context_object_name = "students"
    success_url = "/"


class CreateStudent(SuccessMessageMixin, CreateView):
    model = Student
    fields = ['student_id',
              'firstName',
              'lastName',
              'department',
              'mathScore',
              'physicsScore',
              'chemistryScore',
              'biologyScore']
    template_name = "create.html"
    success_url = "/"
    success_message = "Kayit Basarili."


def edit(request, id):
    student = get_object_or_404(Student, student_id=id)
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


class UpdateStudent(InfoMessageMixin, UpdateView):
    model = Student
    template_name = "edit.html"
    fields = ['student_id',
              'firstName',
              'lastName',
              'department',
              'mathScore',
              'physicsScore',
              'chemistryScore',
              'biologyScore']
    success_url = "/"
    info_message = "Guncelleme basarili"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student, student_id=id_)


class DeleteStudent(DeleteView):
    template_name = "delete.html"
    model = Student
    success_url = "/"
    warning_message = "Silme islemi basarili"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Student, student_id=id_)

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.warning_message)
        return super(DeleteStudent, self).delete(request, *args, **kwargs)
