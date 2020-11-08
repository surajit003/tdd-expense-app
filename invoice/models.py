from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Invoice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    gross_amount = models.FloatField()
    tax = models.FloatField()
    net_amount = models.FloatField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return "{} {} {}".format(self.company, self.user, self.net_amount)
