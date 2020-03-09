from django.test import SimpleTestCase
from django.urls import reverse, resolve
from student.views import delete, edit, create, list
from random import randrange


class UrlTest(SimpleTestCase):

    def test_list_url_is_resolved_list(self):
        url = reverse("student:list")
        print(resolve(url))
        self.assertEqual(resolve(url).func, list)

    def test_list_url_is_resolved_create(self):
        url = reverse("student:create")
        print(resolve(url))
        self.assertEqual(resolve(url).func, create)

    def test_list_url_is_resolved_edit(self):
        url = reverse("student:edit", args=[randrange(9999)])
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit)

    def test_list_url_is_resolved_delete(self):
        url = reverse("student:delete", args=[randrange(9999)])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete)
