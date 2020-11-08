from django.contrib import admin
from .models import Invoice

# Register your models here.


@admin.register(Invoice)
class InvoiceModelAdmin(admin.ModelAdmin):
    list_display = ("company", "base_pay", "net_amount", "user", "created_at")
