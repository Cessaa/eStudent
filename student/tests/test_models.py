from django.test import TestCase
from student.models import Student


class ModelTest(TestCase):

    def setUp(self):
        Student.objects.create(
            student_id=1000,
            firstName="Berkay",
            lastName="Tan",
            department="Bilisim",
            mathScore=100,
            physicsScore=0,
            chemistryScore=100,
            biologyScore=0)

    def test_project_is_firstName(self):
        student = Student.objects.get(student_id=1000)
        expected_object_name = f'{student.firstName}'
        self.assertEqual(expected_object_name, "Berkay")

    def test_project_is_calculate(self):
        student = Student.objects.get(student_id=1000)
        self.assertEqual(student.testing_model(), "Berkay Tan 50.0")

    def test_get_absolute_url(self):
        student = Student.objects.get(student_id=1000)
        self.assertEquals(student.get_edit_absolute_url(), '/student/edit/1000')
        self.assertEquals(student.get_delete_absolute_url(), '/student/delete/1000')
