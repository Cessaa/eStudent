from django.shortcuts import render, get_object_or_404
from .forms import StudentForm
from django.http import HttpResponseRedirect
from .models import Student
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView


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

# class DeleteStudent(View):
#     def post(self, request, *args, **kwargs):
#         student = get_object_or_404(Student, student_id=id)
#         student.delete()
#         messages.add_message(request, messages.WARNING, 'Silme işlemi başarılı.')
#         return HttpResponseRedirect('/')

# class UpdateStudent(UpdateView):
#     model = Student
#     template_name = "edit.html"
#     fields = ['student_id',
#               'firstName',
#               'lastName',
#               'department',
#               'mathScore',
#               'physicsScore',
#               'chemistryScore',
#               'biologyScore']
#     success_url = "/"


class DeleteStudent(DeleteView):
    model = Student
    success_url = "/"

    def get_queryset(self):
        queryset = self.get_queryset()
        id = self.kwargs['student_id']
        return get_object_or_404(queryset, id=id)
