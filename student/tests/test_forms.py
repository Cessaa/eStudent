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

    def test_expense_form_invalid_required(self):
        form = StudentForm(data={
            'student_id': 500,
            'firstName': "",
            'lastName': "",
            'department': "",
            'mathScore': 100,
            'physicsScore': 70,
            'chemistryScore': 40,
            'biologyScore': 10
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
        self.assertEqual(form.errors, {
            'firstName': ['This field is required.'],
            'lastName': ['This field is required.'],
            'department': ['This field is required.']
        })

    def test_expense_form_invalid_equal_to_max(self):
        form = StudentForm(data={
            'student_id': 120000,
            'firstName': "Berkay",
            'lastName': "Tan",
            'department': "Bilisim",
            'mathScore': 200,
            'physicsScore': 150,
            'chemistryScore': 150,
            'biologyScore': 101
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)
        self.assertEqual(form.errors, {
            'student_id': ['Ensure this value is less than or equal to 9999.'],
            'mathScore': ['Ensure this value is less than or equal to 100.'],
            'physicsScore': ['Ensure this value is less than or equal to 100.'],
            'chemistryScore': ['Ensure this value is less than or equal to 100.'],
            'biologyScore': ['Ensure this value is less than or equal to 100.'],
        })
