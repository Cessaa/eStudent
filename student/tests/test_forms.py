from django.test import TestCase
from student.forms import StudentForm


class ModelTest(TestCase):

    def test_expense_form_valid_data(self):
        form = StudentForm(data={
            'student_id': 500,
            'firstName': "Emre",
            'lastName': "Tan",
            'department': "Panama",
            'mathScore': 100,
            'physicsScore': 70,
            'chemistryScore': 40,
            'biologyScore': 10
        })

        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = StudentForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 8)
