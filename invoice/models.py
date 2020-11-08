from django.db import models
from django.contrib.auth import get_user_model
from django_countries.fields import CountryField

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


class TaxSetUp(models.Model):
    country = CountryField()
    tax = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.country, self.tax)


class BaseSalarySetUp(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    base_salary = models.FloatField()
    tax = models.ForeignKey(TaxSetUp, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.company, self.base_salary)


class Invoice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    base_pay = models.ForeignKey(BaseSalarySetUp, on_delete=models.CASCADE)
    net_amount = models.FloatField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

    def __str__(self):
        return "{} {} {}".format(self.company, self.user, self.net_amount)

    def save(self, *args, **kwargs):
        self.net_amount = self.base_pay.base_salary - float(
            self.base_pay.tax.tax * self.base_pay.base_salary
        )
        return super(Invoice, self).save(*args, **kwargs)
