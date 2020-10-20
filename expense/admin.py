from django.contrib import admin
from .models import Expense

# Register your models here.


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("expense_id", "total", "updated_at")
