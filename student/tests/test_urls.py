from django.test import SimpleTestCase
from django.urls import reverse, resolve
from student.views import delete, edit, CreateView, ListView
from random import randrange


class UrlTest(SimpleTestCase):

    def test_list_url_is_resolved_list(self):
        url = reverse("student:list")
        self.assertEqual(resolve(url).func, ListView)

    def test_list_url_is_resolved_create(self):
        url = reverse("student:create")
        self.assertEqual(resolve(url).func, CreateView)

    def test_list_url_is_resolved_edit(self):
        url = reverse("student:edit", args=[randrange(9999)])
        self.assertEqual(resolve(url).func, edit)

    def test_list_url_is_resolved_delete(self):
        url = reverse("student:delete", args=[randrange(9999)])
        self.assertEqual(resolve(url).func, delete)
