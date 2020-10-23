from expense.models import Expense
from django.test import TestCase
from datetime import datetime
from django.urls import reverse


class ExpenseModelTest(TestCase):
    def setUp(self) -> None:
        self.expense = Expense.objects.create(
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
        now = datetime.now().strftime("%Y-%m")
        self.yr, self.month = now.split("-")

    def test_expense_str(self):
        self.assertEqual(str(self.expense), self.expense.expense_id)

    def test_get_year(self):
        self.assertEqual(self.expense.get_year(), int(self.yr))

    def test_get_month(self):
        self.assertEqual(self.expense.get_month(), int(self.month))

    def test_get_absolute_url(self):
        self.assertEqual(
            reverse("expense:expense_detail", args=[str(self.expense.expense_id)]),
            "/expense/{}/detail/".format(self.expense.expense_id),
        )

    def test_for_unique_together_constraint(self):
        with self.assertRaises(Exception):
            Expense.objects.create(
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
