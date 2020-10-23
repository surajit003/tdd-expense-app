from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid
from django.db.models.signals import post_save
from django.urls import reverse


# Create your models here.


class Expense(models.Model):
    expense_id = models.CharField(
        max_length=120, primary_key=True, default=str(uuid.uuid4())
    )
    rent = models.FloatField()
    physio = models.FloatField()
    family = models.FloatField()
    personal = models.FloatField()
    dependent = models.FloatField()
    misc = models.FloatField()
    doctor = models.FloatField()
    gym = models.FloatField()
    saving = models.FloatField()
    extra = models.TextField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Expense Detail")
        verbose_name_plural = _("Expense Details")
        unique_together = ("month", "year")

    def __str__(self):
        return "{}".format(self.expense_id)

    def get_year(self):
        return self.created_at.year

    def get_month(self):
        return self.created_at.month

    def get_absolute_url(self):
        return reverse("expense:expense_detail", args=[str(self.expense_id)])


def update_date_year(sender, instance, **kwargs):
    Expense.objects.filter(expense_id=instance.expense_id).update(
        month=instance.get_month(),
        year=instance.get_year(),
        total=instance.rent
        + instance.physio
        + instance.family
        + instance.personal
        + instance.dependent
        + instance.misc
        + instance.doctor
        + instance.gym
        + instance.saving,
    )


post_save.connect(update_date_year, sender=Expense)
