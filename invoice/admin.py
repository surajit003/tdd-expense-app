from django.contrib import admin
from .models import Invoice, Company, TaxSetUp, BaseSalarySetUp

# Register your models here.


@admin.register(Invoice)
class InvoiceModelAdmin(admin.ModelAdmin):
    list_display = ("company", "base_pay", "net_amount", "user", "created_at")


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(TaxSetUp)
class TaxSetUpModelAdmin(admin.ModelAdmin):
    list_display = ("country", "tax")


@admin.register(BaseSalarySetUp)
class BaseSalarySetUpModelAdmin(admin.ModelAdmin):
    list_display = ("company", "base_salary", "tax")
