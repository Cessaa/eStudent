from django.test import TestCase, Client
from django.urls import reverse
from student.models import Student
import json


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("student:list")
        self.edit_url = reverse("student:edit", args=[500])
        self.delete_url = reverse("student:delete", args=[500])
        self.create_url = reverse("student:create")

        self.student = Student.objects.create(

            student_id=500,
            firstName="Mert",
            lastName="Sile",
            department="Development",
            mathScore=60,
            physicsScore=77,
            chemistryScore=18,
            biologyScore=29)

    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list.html")

    def test_project_edit_GET(self):
        response = self.client.get(self.edit_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit.html")

    def test_project_edit_CREATE(self):
        response = self.client.post(self.create_url, {
            "student_id": 600,
            "firstName": "Haluk",
            "lastName": "Tan",
            "department": "Development",
            "mathScore": 60,
            "physicsScore": 77,
            "chemistryScore": 18,
            "biologyScore": 29})

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Student.objects.get(student_id=600).firstName, "Haluk")

    def test_project_edit_no_data_CREATE(self):
        response = self.client.post(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Student.objects.count(), 1)

    def test_project_DELETE(self):
        response = self.client.delete(self.delete_url, json.dumps({
            "student_id": 500
        }))

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Student.objects.count(), 0)
