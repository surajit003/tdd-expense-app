from django.test import TestCase
from django.urls import resolve, reverse
from django.test.client import Client
from .models import Expense
from .views import HomeView
from .forms import ExpenseForm

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

    def test_create_expense_and_retrieve_detail(self):
        expense = Expense.objects.create(
            rent=10,
            physio=20,
            family=10,
            personal=20,
            dependent=5,
            misc=10,
            doctor=10,
            gym=10,
            saving=10,
        )
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(
            str(expense), "{}-{}".format(expense.expense_id, expense.total)
        )
        self.assertEqual(expense.total, 105)

    def test_save_post_request(self):
        url = reverse("expense:home")
        data = dict(
            rent=10,
            physio=20,
            family=10,
            personal=20,
            dependent=5,
            misc=100,
            doctor=10,
            gym=10,
            saving=10,
        )
        self.client.post(url, data=data)
        expense = Expense.objects.first()
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(expense.total, 195.0)

    def test_redirect_after_post_request(self):
        url = reverse("expense:home")
        data = dict(
            rent=10,
            physio=20,
            family=10,
            personal=20,
            dependent=5,
            misc=100,
            doctor=10,
            gym=10,
            saving=10,
        )
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed("expense/detail.html")

    def test_form_is_invalid_with_invalid_data(self):
        data = dict(
            rent=10,
            physio=20,
            family=10,
            personal=20,
            dependent=5,
            misc=10,
            doctor=10,
            gym=10,
        )
        form = ExpenseForm(data=data)
        self.assertFalse(form.is_valid())

    def test_display_total_and_expense_id(self):
        expense = Expense.objects.create(
            rent=10,
            physio=20,
            family=10,
            personal=20,
            dependent=5,
            misc=10,
            doctor=10,
            gym=10,
            saving=10,
        )
        url = reverse(
            "expense:expense_detail", kwargs={"expense_id": expense.expense_id}
        )

        response = self.client.get(url)
        self.assertIn(str(expense.expense_id), response.content.decode())
        self.assertIn(str(expense.total), response.content.decode())
