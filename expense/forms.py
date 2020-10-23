from django.forms import ModelForm
from .models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        exclude = ("total", "updated_at", "created_at", "expense_id", "month", "year")
