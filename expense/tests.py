from django.test import TestCase
from django.urls import resolve,reverse
from .views import HomeView
# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve(reverse('expense:home'))
        self.assertEqual(found.func,HomeView)

