from django.test import TestCase
from django.core.urlresolvers import resolve
from quiz.views import index

class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, index)
