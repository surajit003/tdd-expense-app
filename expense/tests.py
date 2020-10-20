from django.test import TestCase
from django.urls import resolve, reverse
from django.test.client import Client
from .views import HomeView

# Create your tests here.


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve(reverse("expense:home"))
        self.assertEqual(found.func, HomeView)

    def test_home_page_returns_correct_template(self):
        url = reverse("expense:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "expense/home.html")
