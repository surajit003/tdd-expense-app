from expense.utils import render_to_pdf
from expense.models import Expense
from django.test import TestCase


class TestUtils(TestCase):
    def test_render_to_pdf_returns_correct_response_type(self):
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

        res = render_to_pdf("expense/expense_pdf.html", expense.__dict__)
        self.assertEqual(res["content-type"], "application/pdf")
